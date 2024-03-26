from decimal import Decimal, ROUND_HALF_UP
from rest_framework import generics
from tools_rest.response_view import success, bad_request
from simalfa.models.serviceitem import ServiceItem
from simulation.serializers import GetFilterServiceItemSerializer, ServiceItemOutputSerializer, DescriptionSerializer, DataServiceInputSerializer, OutputModels
from simulation.enums import TypeService
from simalfa.enums import TypeMetric
from drf_yasg.utils import swagger_auto_schema
from tools_rest.swagger_view import SwaggerResultViewModel
from simulation.models.simulation import SimulationEntity, SimulationSerializer, SimulationGetSerializer
from simulation.models.service import ServiceEntity
from simulation.models.metrics import MetricsEntity

# Create your views here.
class GetServicesItemsForTypeView(generics.ListAPIView):
    queryset = ServiceItem.objects.filter(active=True)
    serializer_class = GetFilterServiceItemSerializer
    
    @swagger_auto_schema(query_serializer=GetFilterServiceItemSerializer, responses={200: SwaggerResultViewModel(ServiceItemOutputSerializer, True,
    {
        'items': (True, DescriptionSerializer),
    }).openapi}, tags=['simulation'])
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            type_service:str = self.request.query_params.get('type_service', None)
            type_service_enum = TypeService[type_service.upper()]
        except:
            return bad_request('Tipo de serviço informado é inválido')
        
        if type_service_enum == TypeService.FCL:
            queryset = queryset.filter(formula_fcl__isnull=False)
        else:
            queryset = queryset.filter(formula_lcl__isnull=False)
        
        result = {}
        for service_item in sorted(queryset, key=lambda x: tuple(map(int, x.code.split('.')))):
            code_split = service_item.code.split('.')
            if len(code_split) > 0:
                code_prefix = code_split[0]
                if type_service_enum == TypeService.FCL:
                    formula = service_item.formula_fcl
                else:
                    formula = service_item.formula_lcl
                
                metrics = []
                for metric in formula.metrics.all().exclude(type=TypeMetric.IMUTAVEL.value):
                    return_metric = {
                        'id': metric.id,
                        'description': metric.description,
                        'type': metric.type,
                        'service': metric.service,
                        'value': '0.00000'
                    }
                    metrics.append(return_metric)
                    print(metric.type)
                               
                descriptions = result.get(code_prefix, [])
                descriptions.append({'code': service_item.code, 'description': service_item.description, 'metrics': metrics})
                result[code_prefix] = descriptions
        
        service_item_data = [{'service': code_group, 'items': result[code_group]} for code_group in result]
        
        serializer = ServiceItemOutputSerializer(data=service_item_data, many=True)
        if serializer.is_valid():
            return success(serializer.data)
        
class GenerateView(generics.CreateAPIView):
    queryset = ServiceEntity.objects.all()
    serializer_class = DataServiceInputSerializer
    
    def post(self, request, *args, **kwargs):
        validator = DataServiceInputSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        
        type_service:str = request.data.get('type_service', None)
        type_service_enum = TypeService[type_service.upper()]
        
        list = []
        metrics_list = []
        total = Generate_Simulation(request.data, type_service_enum, list, metrics_list)
        
        service_items_id = []
        for metric_item in metrics_list:
            metrics = metric_item.get('metrics', [])
            code = metric_item.get('code', '0')
            new_service = ServiceEntity.objects.create(code=code)
            for metric in metrics:
                metric.save()
        
            new_service.items.set(metrics)
            service_items_id.append(new_service.pk)
        
        last = SimulationEntity.objects.last()
        last_id = last.pk + 1 if last else 1
        request.data['services'] = service_items_id
        request.data['auto_number'] = last_id
        
        simulation_serializer = SimulationSerializer(data=request.data)
        simulation_serializer.is_valid(raise_exception=True)
        simulation_serializer.save()
        
        request.data['services'] = list
        request.data['total'] = total
        request.data['auto_number'] = str(last_id).zfill(10)
        request.data['date_register'] = simulation_serializer.data.get('date_register')
        
        serializer_return = OutputModels.DataClientSimulationOutputSerializer(request.data)
        return success(serializer_return.data)
    
class GetView(generics.ListAPIView):
    queryset = SimulationEntity.objects.alast()
    
    def get(self, request, *args, **kwargs):
        email = kwargs['email']
        
        simulations_user = SimulationEntity.objects.filter(email=email)
        simulations_list = []
        for simulation in simulations_user:
            enum_type = TypeService(simulation.type_service)
            
            simulation_service_list = []
            serializer = SimulationGetSerializer(simulation).data
            serializer['total'] = Generate_Simulation(serializer, enum_type, simulation_service_list)
            serializer['services'] = simulation_service_list
            serializer_return = OutputModels.DataClientSimulationOutputSerializer(serializer).data
            simulations_list.append(serializer_return)

        result = OutputModels.DataClientSimulationOutputSerializer(simulations_list, many=True).data
        return success(result)
                   
def Generate_Simulation(input_model, type_service_enum, listing, metrics_list:list = None) -> str:
    total = Decimal(0)
    prefixe_atuality = None
    total_service = Decimal(0)
    services_input = input_model.get('services', None)
    if not services_input:
        return bad_request("Nenhum serviço foi informado para gerar uma simulação.")
    
    services = ServiceItem.objects.filter(active=True)
    if not services:
        return bad_request("Nenhum serviço foi encontrado para gerar uma simulação.")
    
    services_metrics = {}
    for input in sorted(services_input, key=lambda x: tuple(map(int, x.get('code').split('.')))):
        code:str = input.get('code', "0")
        prefixe = code.split('.')[0]
        if not prefixe_atuality:
            prefixe_atuality = prefixe
        try:
            service = services.get(code=code)
        except:
            continue
        
        if not 'tenant' in input_model:
            input_model['tenant'] = service.tenant.pk

        if type_service_enum == TypeService.FCL:
            formula_service = service.formula_fcl
        else:
            formula_service = service.formula_lcl

        expression = formula_service.expression

        for service_item_metric in service.service_item_metrics.all():
            if service_item_metric.metric.type == TypeMetric.IMUTAVEL.value:
                expression = expression.replace(service_item_metric.metric.service, str(service_item_metric.value))

        amount = 1
        metrics_input = input.get('metrics', None)
        
        metric_list_exist = metrics_list is not None
        if metric_list_exist:
                metrics_internal_list = []
                
        for metric_input in metrics_input:
            id = metric_input.get('id_metric', metric_input.get('id', 0))

            try:
                metric = formula_service.metrics.get(pk=id)
            except:
                return bad_request(f'Metrica não pode ser localizada.')

            value = metric_input.get('value', 0.00000)
            expression = expression.replace(metric.service, str(value))

            if amount == 1 and (metric.service in ['QTDE', 'ND', 'HORA']):
                amount = value

            if metric.service == 'CIF':
                input_model['cif'] = value

            if metric_list_exist:
                new_metric = MetricsEntity(id_metric=metric, value=value)
                metrics_internal_list.append(new_metric)

        if metric_list_exist:
            metrics_list.append({'code': code, 'metrics': metrics_internal_list})
        
        import locale
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        result_expression = eval(expression)
        result_expression = Decimal(result_expression).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

        unity = result_expression / Decimal(amount) if Decimal(amount) > 0 and result_expression > 0 else 0
        value_unity = locale.format_string("%.5f", unity, grouping=True)
        total_value = locale.format_string("%.5f", result_expression, grouping=True)

        service_atuality:dict = services_metrics.get(prefixe, {})
        if not service_atuality:
            service_atuality = { 'service': prefixe }
        
        items:list = service_atuality.get('items', [])
        data = {
            'code': service.code,
            'amount': amount,
            'unity': value_unity,
            'description': service.description,
            'value': total_value
        }
        
        items.append(data)
        service_atuality['items'] = items
        services_metrics[prefixe] = service_atuality
        
        if prefixe_atuality != prefixe:
            service_pass:dict = services_metrics.get(prefixe_atuality, {})
            service_pass['total'] = locale.format_string("%.5f", total_service, grouping=True)
            services_metrics[prefixe_atuality] = service_pass
            listing.append(services_metrics[prefixe_atuality])
            total_service = Decimal(0)
            prefixe_atuality = prefixe
        
        total_service += result_expression 
        
        total += result_expression
    
    service_pass:dict = services_metrics.get(prefixe_atuality, {})
    service_pass['total'] = locale.format_string("%.5f", total_service, grouping=True)
    services_metrics[prefixe_atuality] = service_pass
    listing.append(services_metrics[prefixe_atuality])
    
    return locale.format_string("%.5f", total, grouping=True)