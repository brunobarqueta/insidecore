from rest_framework import generics
from django.http.response import Http404
from tools_rest.response_view import success, bad_request
from rest_framework.permissions import IsAuthenticated
from simalfa.models.service import (Service, ServiceSerializer)
from simalfa.models.item import (Items, ItemsSerializer)
from simalfa.models.tenant import (Tenant, TenantAllPropertiesSerializer, TenantListCreateSerializer, TenantGetAlterSerializer)
from simalfa.models.metrics import (Metrics, MetricsAllPropertiesSerializer, MetricsListCreateSerializer, MetricsGetAlterSerializer)
from simalfa.models.formula import (Formula, FormulaAllPropertiesSerializer, FormulaListCreateSerializer, FormulaGetAlterSerializer)
from simalfa.models.serviceitem import (ServiceItem, ServiceItemAllPropertiesSerializer, ServiceItemListCreateSerializer, ServiceItemGetAlterSerializer)

#Criar responses do swager
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers

def map_field_type(field, serializerMethodField = None):
    if(type(field) == serializers.SerializerMethodField) and serializerMethodField:
        (isList, model) = serializerMethodField[field.field_name]
        openapi_result = openapi.Schema(type=openapi.TYPE_OBJECT, properties={field.name: map_field_type(field._field) for field in model()})
        if isList:
            openapi_result = openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi_result)
        return openapi_result
    
    field_mapping = {
        serializers.CharField: openapi.TYPE_STRING,
        str: openapi.TYPE_STRING,
        
        serializers.IntegerField: openapi.TYPE_INTEGER,
        int: openapi.TYPE_INTEGER,
        
        serializers.BooleanField: openapi.TYPE_BOOLEAN,
        bool: openapi.TYPE_BOOLEAN,
        
        serializers.SerializerMethodField: openapi.TYPE_OBJECT
        # Adicione mais mapeamentos conforme necessário para outros tipos de campos
    }
    mapped_field = field_mapping.get(type(field), openapi.TYPE_STRING)
    return openapi.Schema(type=mapped_field)

class ResultViewModel:
    def __init__(self, obj, list = False, methodField = None):
        if hasattr(obj, 'fields'):  # Verifica se é um serializador
            openapi_result = openapi.Schema(type=openapi.TYPE_OBJECT, properties={field.name: map_field_type(field._field, methodField) for field in obj()})
            if list:
                openapi_result = openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi_result)
        else:  # Caso seja um tipo primitivo
            properties = map_field_type(obj)
            openapi_result = openapi.Schema(type=properties)
        
        self.openapi = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                #'result': openapi.Schema(type=openapi.TYPE_OBJECT, properties=properties),
                'result': openapi_result,
                'errors': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            }
        )
#Fim criação responses do swager

# Create your views here.
        
class MetricsCrudView:
    class MetricsGetCreateView(generics.ListCreateAPIView):
        queryset = Metrics.objects.all()
        serializer_class = MetricsListCreateSerializer
        #permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: ResultViewModel(MetricsAllPropertiesSerializer, True, {'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['metrics'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = MetricsAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: ResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['metrics'])
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = MetricsAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class MetricsGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = Metrics.objects.all()
        serializer_class = MetricsGetAlterSerializer
        #permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method == 'GET' or self.request.method == 'PATCH':
                return None
            else:
                return MetricsGetAlterSerializer
    
        @swagger_auto_schema(responses={200: ResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['metrics'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = MetricsAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=MetricsGetAlterSerializer,responses={200: ResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['metrics'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = MetricsAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
    
        @swagger_auto_schema(responses={200: ResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['metrics'])
        def patch(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = MetricsAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
        
class FormulaCrudView:
    class FormulaGetCreateView(generics.ListCreateAPIView):
        queryset = Formula.objects.all()
        serializer_class = FormulaListCreateSerializer
        #permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: ResultViewModel(FormulaAllPropertiesSerializer, True, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['formulas'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = FormulaAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: ResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['formulas'])
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = FormulaAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class FormulaGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = Formula.objects.all()
        serializer_class = FormulaGetAlterSerializer
        #permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method == 'GET' or self.request.method == 'PATCH':
                return None
            else:
                return FormulaGetAlterSerializer
    
        @swagger_auto_schema(responses={200: ResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['formulas'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = FormulaAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=FormulaGetAlterSerializer,responses={200: ResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['formulas'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = FormulaAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
    
        @swagger_auto_schema(responses={200: ResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['formulas'])
        def patch(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = FormulaAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
        
class ServiceItemCrudView:
    class ServiceItemGetCreateView(generics.ListCreateAPIView):
        queryset = ServiceItem.objects.all()
        serializer_class = ServiceItemListCreateSerializer
        #permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: ResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'formula_fcl':(False, FormulaAllPropertiesSerializer), 
                'formula_lcl':(False, FormulaAllPropertiesSerializer)
            }).openapi}, tags=['service-items'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = ServiceItemAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: ResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'formula_fcl':(False, FormulaAllPropertiesSerializer), 
                'formula_lcl':(False, FormulaAllPropertiesSerializer)
            }).openapi}, tags=['service-items'])
        def post(self, request, *args, **kwargs):
            group_code = request.data.get('group_code', None)
            if group_code:
                group = [item for item in Service().get_defaults_groups() if item.code == group_code]
                
            if not group_code or not group:
                return bad_request('Codigo de grupo informado é inválido.')
            
            item_code = request.data.get('item_code', None)
            if item_code:
                item = [item for item in Items.get_defaults_items() if item.code == item_code and item.code_group == group_code]
            
            if not item_code or not item:
                return bad_request('Codigo de item informado é inválido.')
            
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = ServiceItemAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class ServiceItemGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = ServiceItem.objects.all()
        serializer_class = ServiceItemGetAlterSerializer
        #permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method == 'GET' or self.request.method == 'PATCH':
                return None
            else:
                return ServiceItemGetAlterSerializer
    
        @swagger_auto_schema(responses={200: ResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'formula_fcl':(False, FormulaAllPropertiesSerializer), 
                'formula_lcl':(False, FormulaAllPropertiesSerializer)
            }).openapi}, tags=['service-items'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = ServiceItemAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=ServiceItemGetAlterSerializer, responses={200: ResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'formula_fcl':(False, FormulaAllPropertiesSerializer), 
                'formula_lcl':(False, FormulaAllPropertiesSerializer)
            }).openapi}, tags=['service-items'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = ServiceItemAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
            
        @swagger_auto_schema(responses={200: ResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'formula_fcl':(False, FormulaAllPropertiesSerializer), 
                'formula_lcl':(False, FormulaAllPropertiesSerializer)
            }).openapi}, tags=['service-items'])
        def patch(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = ServiceItemAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)

class TenantCrudView:
    class TenantGetCreateView(generics.ListCreateAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantListCreateSerializer
        #permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: ResultViewModel(TenantAllPropertiesSerializer, True).openapi}, tags=['tenants'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = TenantAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
    
        @swagger_auto_schema(responses={200: ResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['tenants'])
        def post(self, request, *args, **kwargs):
            serializer = TenantAllPropertiesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
    
    class TenantGetPutView(generics.RetrieveUpdateAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantGetAlterSerializer
        #permission_classes = [IsAuthenticated]
        
        def get_serializer_class(self):
            if self.request.method == 'GET' or self.request.method == 'PATCH':
                return None
            else:
                return TenantGetAlterSerializer     
        
        @swagger_auto_schema(responses={200: ResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['tenants'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = TenantAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=TenantGetAlterSerializer,responses={200: ResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['tenants'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = TenantAllPropertiesSerializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return success(serializer.data)
           
        @swagger_auto_schema(responses={200: ResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['tenants']) 
        def patch(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = TenantAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
        
class ServicesCrudView:
    class GetGroupsView(generics.ListAPIView):
        queryset = Service().get_defaults_groups()
        serializer_class = ServiceSerializer
        #permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: ResultViewModel(ServiceSerializer, True).openapi}, tags=['groups'])
        def get(self, request, *args, **kwargs):
            groups = self.get_queryset()
            serializer = self.serializer_class(groups, many=True)
            return success(serializer.data)
    
    class GetItensForGroupsView(generics.RetrieveAPIView):
        queryset = Items().get_defaults_items()
        serializer_class = ItemsSerializer
        lookup_field = 'code_group'
        #permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: ResultViewModel(ItemsSerializer, True).openapi}, tags=['items'])
        def get(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            items = [item for item in queryset if item.code_group == kwargs.get(self.lookup_field)]
            if not items:
                raise Http404()
            serializer = self.serializer_class(items, many=True)
            return success(serializer.data)