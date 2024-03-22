from rest_framework import generics
from tools_rest.response_view import success, bad_request
from simalfa.models.serviceitem import ServiceItem
from simulation.serializers import GetFilterServiceItemSerializer, ServiceItemOutputSerializer, DescriptionSerializer, DataServiceInputSerializer
from simulation.enums import TypeService
from simalfa.enums import TypeMetric
from drf_yasg.utils import swagger_auto_schema
from tools_rest.swagger_view import SwaggerResultViewModel

import random
from decimal import Decimal

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
                for serv_item_metric in service_item.service_item_metrics.all():
                    try:
                        if formula.metrics.filter(pk=serv_item_metric.metric_id).exclude(type=TypeMetric.IMUTAVEL).first():
                            metric = {
                                "id": serv_item_metric.metric.id,
                                "type": serv_item_metric.metric.type,
                                "service": serv_item_metric.metric.service,
                                "value": serv_item_metric.value
                            }
                            metrics.append(metric)
                    except:
                        continue            
                descriptions = result.get(code_prefix, [])
                descriptions.append({'code': service_item.code, 'description': service_item.description, 'metrics': metrics})
                result[code_prefix] = descriptions
        
        service_item_data = [{'service': code_group, 'items': result[code_group]} for code_group in result]
        
        serializer = ServiceItemOutputSerializer(data=service_item_data, many=True)
        if serializer.is_valid():
            return success(serializer.data)
        
class GenerateView(generics.CreateAPIView):
    queryset = ServiceItem.objects.filter(active=True)
    serializer_class = DataServiceInputSerializer
    
    def post(self, request, *args, **kwargs):
        #Validar entradas.
        #tt = DataServiceInputSerializer(data=request.data)
        #tt.is_valid(raise_exception=True)
        
        try:
            type_service:str = request.data.get('type_service', None)
            type_service_enum = TypeService[type_service.upper()]
        except:
            return bad_request('Tipo de serviço informado é inválido')
        
        services_input = request.data.get('services', None)
        if not services_input:
            return bad_request("Nenhum serviço foi informado para gerar uma simulação.")
        
        if type_service_enum == TypeService.FCL:
            services = ServiceItem.objects.filter(active=True, formula_fcl__isnull=False)
        else:
            services = ServiceItem.objects.filter(active=True, formula_lcl__isnull=False)
        
        if not services:
            return bad_request("Nenhum serviço foi encontrado para gerar uma simulação.")
        
        list = []
        for input in services_input:
            random_decimal = round(random.uniform(10.0, 1000.0), 5)
            code = input.get('code', "0")
            data = {
                'code': code,
                'description': 'mock description',
                'value': random_decimal
            }
            list.append(data)
            
            #amount = input.get('amount', 0)
            #service = services.filter(code=code).first()
            #if not service:
            #    return bad_request('Serviço não foi encontrado.')
        
        return success(list)