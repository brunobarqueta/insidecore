from rest_framework import generics
from tools_rest.response_view import success, bad_request
from simalfa.models.serviceitem import ServiceItem
from simulation.serializers import GetFilterServiceItemSerializer, ServiceItemOutputSerializer, DescriptionSerializer
from simulation.enums import TypeService
from drf_yasg.utils import swagger_auto_schema
from tools_rest.swagger_view import SwaggerResultViewModel

# Create your views here.
class GetServicesItemsForType(generics.ListAPIView):
    queryset = ServiceItem.objects.filter(active=True)
    serializer_class = GetFilterServiceItemSerializer
    
    @swagger_auto_schema(query_serializer=GetFilterServiceItemSerializer, responses={200: SwaggerResultViewModel(ServiceItemOutputSerializer, True,
    {
        'description': (True, DescriptionSerializer),
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
        for service_item in queryset.order_by('code'):
            code_split = service_item.code.split('.')
            if len(code_split) > 0:
                code_prefix = code_split[0]
                descriptions = result.get(code_prefix, [])
                descriptions.append({'code': service_item.code, 'description': service_item.description})
                result[code_prefix] = descriptions
        
        service_item_data = [{'service': code_group, 'description': result[code_group]} for code_group in result]
        
        serializer = ServiceItemOutputSerializer(data=service_item_data, many=True)
        if serializer.is_valid():
            return success(serializer.data)