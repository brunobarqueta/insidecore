from decimal import Decimal, ROUND_HALF_UP
import os
from rest_framework import generics
from tools_rest.response_view import success, bad_request
from backend.settings import STATIC_ROOT
from simalfa.models.serviceitem import ServiceItem
from simalfa.models.tenant import Tenant
from simulation.serializers import GetFilterServiceItemSerializer, ServiceItemOutputSerializer, DescriptionSerializer, DataServiceInputSerializer, OutputModels
from simulation.enums import TypeService
from simalfa.enums import TypeMetric
from drf_yasg.utils import swagger_auto_schema
from tools_rest.swagger_view import SwaggerResultViewModel
from simulation.models.simulation import SimulationEntity, SimulationSerializer, SimulationGetSerializer
from simulation.models.service import ServiceEntity
from simulation.models.metrics import MetricsEntity
import base64
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import locale
from datetime import datetime


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
        request.data['name'] = request.data['name'].title()
        
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
        
        data_return = OutputModels.DataClientSimulationOutputSerializer(request.data).data
        tenant = Tenant.objects.get(pk=request.data['tenant'])
        data_return['pdf'] = Generate_PDF(data_return, tenant)
        return success(data_return)
    
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
        
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        result_expression = eval(expression)
        result_expression = Decimal(result_expression).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

        unity = result_expression / Decimal(amount) if Decimal(amount) > 0 and result_expression > 0 else 0
        value_unity = locale.format_string("%.2f", unity, grouping=True)
        total_value = locale.format_string("%.2f", result_expression, grouping=True)

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
            service_pass['total'] = locale.format_string("%.2f", total_service, grouping=True)
            services_metrics[prefixe_atuality] = service_pass
            listing.append(services_metrics[prefixe_atuality])
            total_service = Decimal(0)
            prefixe_atuality = prefixe
        
        total_service += result_expression 
        
        total += result_expression
    
    service_pass:dict = services_metrics.get(prefixe_atuality, {})
    service_pass['total'] = locale.format_string("%.2f", total_service, grouping=True)
    services_metrics[prefixe_atuality] = service_pass
    listing.append(services_metrics[prefixe_atuality])
    
    return locale.format_string("%.2f", total, grouping=True)

def Generate_PDF(services, tenant) -> str:
    # Cria um objeto Canvas com o tamanho personalizado
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    y = Generate_Header(p)
    
    #emissor/cliente
    emissor_x = 15
    y -= 15
    emissor_client_width = A4[0]/2-22.5
    emissor_client_height = -65
    client_x = A4[0]/2+7.5
    p.setFillColor('#FCEFDD')
    p.rect(emissor_x, y, emissor_client_width, emissor_client_height, 0, 1)
    p.rect(client_x, y, emissor_client_width, emissor_client_height, 0, 1)
    p.setFillColor(colors.black)
    p.setFont('Helvetica-Bold', 14)
    y -= 14
    p.drawString(emissor_x+7.5, y, 'EMISSOR')
    name_splited = services['name'].split(' ')
    p.drawString(client_x+7.5, y, f'{name_splited[0]} {name_splited[-1]}')
    y -= 4
    p.line(emissor_x+7.5, y, A4[0]/2-15, y)
    p.line(client_x+7.5, y, A4[0]-22.5, y)
    p.setFontSize(14)
    dados_target_x = emissor_x+7.5
    dados_target_y = y-28
    p.drawString(dados_target_x, dados_target_y, tenant.name)
    
    p.setFillColor(colors.black)
    p.setFont('Helvetica-Bold', 14)
    p.setFontSize(9)
    dados_target_x = client_x+7.5
    dados_target_y = y-11
    p.drawString(dados_target_x, dados_target_y, 'NOME DA EMPRESA:')
    p.drawString(dados_target_x, dados_target_y-10, 'CNPJ: 00.000.000/0000-00')
    p.drawString(dados_target_x+120, dados_target_y-10, 'CEP:')
    p.drawString(dados_target_x, dados_target_y-20, 'CIDADE/UF:')
    p.drawString(dados_target_x, dados_target_y-30, 'ENDEREÇO:')
    
    #informações
    p.setFontSize(14)
    y -= 65
    p.drawString(emissor_x, y, 'INFORMAÇÕES')
    y -= 6
    p.line(emissor_x, y, A4[0]-15, y)
    
    data_hora_obj = datetime.strptime(services.get('date_register'), "%Y-%m-%dT%H:%M:%S.%f")
    cif_value = locale.format_string("%.2f", Decimal(services.get('cif', '0')), grouping=True)
    data_hora_formatada = data_hora_obj.strftime("%d/%m/%Y %H:%M")
    
    data = [
        ["Número Simulação", services.get('auto_number', 'NA')],
        ["DATA", data_hora_formatada],
        ["E-MAIL", services.get('email', 'NA')],
        ["Valor CIF", f"RS {cif_value}"]
    ]
    
    table = Table(data, emissor_client_width/2)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ('#FCEFDD')),
        ('TEXTCOLOR', (0, 0), (-1, -1), (0, 0, 0)),
        ('ALIGN', (-1, 0), (-1, -1), 'CENTER'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)), 
        ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
    ])
    table.setStyle(style)
    table.wrapOn(p, 0, 0)
    y -= 80
    table.drawOn(p, emissor_x, y)
    
    #Indicador de simulação
    p.setFillColor(colors.red)
    p.setFont('Helvetica-Bold', 14)
    p.rotate(15)
    p.drawString(client_x+25 * 10, y - 105, 'SIMULAÇÃO')
    p.rotate(-15)
    
    y -= 40
    for service in services.get('services', []):
        code_service = service.get('service', '1')
        if code_service == '1':
            name_service = 'SERVIÇOS INERENTES'
        elif code_service == '2':
            name_service = 'SERVIÇOS COMPLEMENTARES'
        elif code_service == '3':
            name_service = 'SERVIÇOS ACESSÓRIOS'
        else:
            name_service = 'SERVIÇOS DIVERSOS'
        
        if y < 100:
            p.showPage()
            y = Generate_Header(p) - 42
        
        p.setFillColor('#AEAEAE')
        p.rect(emissor_x, y, A4[0] - 30, 28, 1, 1)
        p.setFillColor('#FFFFFF')
        p.setFontSize(14)
        y += 9
        p.drawString(emissor_x + 5, y, name_service)
        y -= 29
        
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), ('#FCEFDD')),
            ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('LEFTPADDING', (0, 0), (0, 0), 10),
            ('LEFTPADDING', (0, 1), (0, -1), 15),
            ('TOPPADDING', (0, 0), (-1, 0), -2),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
            ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
        ])
        
        items = service.get('items')
        linha = 1
        data = [['SERVIÇO', 'QTDE', 'UNIT.', 'TOTAL']]
        height_row = 20
        for item in items:
            number_float = float(item.get('amount', '0'))
            amount = int(number_float) if number_float.is_integer() else number_float
            
            row = [
                item.get('description', ''),
                amount,
                f"RS {item.get('unity', '0.00')}",
                f"RS {item.get('value', '0.00')}"
            ]
            data.append(row)
            linha+=1
            y -= height_row
            if y < 50:
                table = Table(data, colWidths=[A4[0]-230,50,70,80], rowHeights=height_row)
                table.setStyle(style)
                table.wrapOn(p, 0, 0)
                table.drawOn(p, emissor_x, y)
                data = [['SERVIÇO', 'QTDE', 'UNIT.', 'TOTAL']]
                p.showPage()
                y = Generate_Header(p) - 35
                print('teste')
        
        table = Table(data, colWidths=[A4[0]-230,50,70,80], rowHeights=height_row)
        table.setStyle(style)
        table.wrapOn(p, 0, 0)
        table.drawOn(p, emissor_x, y) 
        
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 0), (-1, -1), ('#FCEFDD')),
            ('BACKGROUND', (0, 1), (-1, -1), ('#707070')),
            ('ALIGN', (0, 1), (-1, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (0, 0), 15),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.white),
            ('FONTSIZE', (0, 1), (-1, -1), 14),
            ('TOPPADDING', (0, 1), (-1, -1), -2),
            ('LEFTPADDING', (0, 1), (0, 0), 30),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)), 
            ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)), 
        ])
            
        data = [
            [services.get('', '')],
            [f"VALOR TOTAL: R$ {service.get('total', '0,00')}"]
        ]
        
        table = Table(data, colWidths=[A4[0]-30], rowHeights=[height_row, 25])
        table.setStyle(style)
        table.wrapOn(p, 0, 0)
        y -= height_row * 2 + 5
        table.drawOn(p, emissor_x, y+1)
        y -= 20 + height_row 
    
    data=[[f"VALOR TOTAL A PAGAR: R$ {services.get('total', '0,00')}"]]
    table = Table(data, A4[0] - 30, 40)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ('#FF7A00')),
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, 0), -2),
        ('FONTSIZE', (0, 0), (-1, -1), 14), 
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
    ])
    table.setStyle(style)
    table.wrapOn(p, 0, 0)
    y -= 15
    if y < 80:
        p.showPage()
        y = Generate_Header(p) - 55
    table.drawOn(p, emissor_x, y) 
    
    p.showPage()
    p.save()

    pdf_content = buffer.getvalue()
    base64_str = base64.b64encode(pdf_content).decode()
    return base64_str

def Generate_Header(canva) -> float:
    canva.setFillColor('#FF7A00')
    y = A4[1] - 42
    canva.rect(0, y, A4[0], 42, 0, 1)
    
    image_path = os.path.join(STATIC_ROOT, "img", "logo.png")
    canva.drawImage(image_path, 15, y, width=97.2, height=38.8, mask='auto')
    return y