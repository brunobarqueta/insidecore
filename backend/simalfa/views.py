from rest_framework import generics
from django.http.response import Http404
from tools_rest.response_view import success, bad_request
from tools_rest.swagger_view import SwaggerResultViewModel
from rest_framework.permissions import IsAuthenticated
from simalfa.models.service import (Service, ServiceSerializer)
from simalfa.models.item import (Items, ItemsSerializer)
from simalfa.models.tenant import (Tenant, TenantAllPropertiesSerializer, TenantListCreateSerializer, TenantGetAlterSerializer)
from simalfa.models.metrics import (Metrics, MetricsAllPropertiesSerializer, MetricsListCreateSerializer, MetricsGetAlterSerializer)
from simalfa.models.formula import (Formula, FormulaAllPropertiesSerializer, FormulaListCreateSerializer, FormulaGetAlterSerializer, FormulaPropertiesSerializer)
from simalfa.models.serviceitem import (ServiceItem, ServiceItemAllPropertiesSerializer, ServiceItemListCreateSerializer, ServiceItemGetAlterSerializer)
from simalfa.models.serviceitemmetrcs import (ServiceItemMetrics, ServiceItemMetricsAllPropertiesSerializer, ServiceItemMetricsListCreateSerializer, ServiceItemMetricsGetAlterSerializer, ServiceItemMetricsPropertiesSerializer)
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
        
class MetricsCrudView:
    class MetricsGetCreateView(generics.ListCreateAPIView):
        queryset = Metrics.objects.all()
        serializer_class = MetricsListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(MetricsAllPropertiesSerializer, True, {'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-metrics'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = MetricsAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-metrics'])
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = MetricsAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class MetricsGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = Metrics.objects.all()
        serializer_class = MetricsGetAlterSerializer
        permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method in ['GET', 'PATCH']:
                return None
            else:
                return MetricsGetAlterSerializer
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-metrics'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = MetricsAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=MetricsGetAlterSerializer,responses={200: SwaggerResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-metrics'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = MetricsAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(MetricsAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-metrics'])
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
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, True, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-formulas'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = FormulaAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-formulas'])
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = FormulaAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class FormulaGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = Formula.objects.all()
        serializer_class = FormulaGetAlterSerializer
        permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method in ['GET', 'PATCH']:
                return None
            else:
                return FormulaGetAlterSerializer
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-formulas'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = FormulaAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=FormulaGetAlterSerializer,responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-formulas'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = FormulaAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField={'tenants': (True, TenantAllPropertiesSerializer)}).openapi}, tags=['admin-formulas'])
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
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer),
                'service_item_metric': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = ServiceItemAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'service_item_metric': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def post(self, request, *args, **kwargs):
            if ServiceItem.objects.filter(code=request.data.get('code')).exists():
                return bad_request('Código informado ja é utilizado')
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = ServiceItemAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class ServiceItemGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = ServiceItem.objects.all()
        serializer_class = ServiceItemGetAlterSerializer
        permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method in ['GET', 'PATCH']:
                return None
            else:
                return ServiceItemGetAlterSerializer
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'service_item_metric': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = ServiceItemAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=ServiceItemGetAlterSerializer, responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'service_item_metric': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = ServiceItemAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
            
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenants': (True, TenantAllPropertiesSerializer), 
                'service_item_metric': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def patch(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = ServiceItemAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)

class ServiceItemMetricsCrudView:
    class ServiceItemMetricsGetPostView(generics.ListCreateAPIView):
        queryset = ServiceItemMetrics.objects.all()
        serializer_class = ServiceItemMetricsListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemMetricsAllPropertiesSerializer, True,
            {
                'tenant': (False, TenantAllPropertiesSerializer), 
                'metrics': (True, ServiceItemMetricsPropertiesSerializer),
            }).openapi}, tags=['admin-service-item-metrics'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = ServiceItemMetricsAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemMetricsAllPropertiesSerializer, True,
            {
                'tenant': (False, TenantAllPropertiesSerializer), 
                'metrics': (True, ServiceItemMetricsPropertiesSerializer),
            }).openapi}, tags=['admin-service-item-metrics'])
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = ServiceItemMetricsAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
    
    class ServiceItemMetricsGetPutPatchView(generics.RetrieveUpdateAPIView):
        queryset = ServiceItemMetrics.objects.all()
        serializer_class = ServiceItemMetricsGetAlterSerializer
        permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method in ['GET', 'PATCH']:
                return None
            else:
                return ServiceItemMetricsGetAlterSerializer
            
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemMetricsAllPropertiesSerializer, True,
            {
                'tenant': (False, TenantAllPropertiesSerializer), 
                'metrics': (True, ServiceItemMetricsPropertiesSerializer),
            }).openapi}, tags=['admin-service-item-metrics'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = ServiceItemMetricsAllPropertiesSerializer(instance)
            return success(serializer.data)
        
        @swagger_auto_schema(request_body=ServiceItemMetricsGetAlterSerializer, responses={200: SwaggerResultViewModel(ServiceItemMetricsAllPropertiesSerializer, True,
            {
                'tenant': (False, TenantAllPropertiesSerializer), 
                'metrics': (True, ServiceItemMetricsPropertiesSerializer),
            }).openapi}, tags=['admin-service-item-metrics'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = ServiceItemMetricsAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemMetricsAllPropertiesSerializer, True,
            {
                'tenant': (False, TenantAllPropertiesSerializer), 
                'metrics': (True, ServiceItemMetricsPropertiesSerializer),
            }).openapi}, tags=['admin-service-item-metrics'])
        def patch(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            serializer = ServiceItemMetricsAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
        
        pass

class TenantCrudView:
    class TenantGetCreateView(generics.ListCreateAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(TenantAllPropertiesSerializer, True).openapi}, tags=['admin-tenants'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = TenantAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['admin-tenants'])
        def post(self, request, *args, **kwargs):
            serializer = TenantAllPropertiesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
    
    class TenantGetPutView(generics.RetrieveUpdateAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantGetAlterSerializer
        permission_classes = [IsAuthenticated]
        
        def get_serializer_class(self):
            if self.request.method in ['GET', 'PATCH']:
                return None
            else:
                return TenantGetAlterSerializer     
        
        @swagger_auto_schema(request_body=None, responses={200: SwaggerResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['admin-tenants'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = TenantAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=TenantGetAlterSerializer,responses={200: SwaggerResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['admin-tenants'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = TenantAllPropertiesSerializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return success(serializer.data)
           
        @swagger_auto_schema(request_body=None, responses={200: SwaggerResultViewModel(TenantAllPropertiesSerializer).openapi}, tags=['admin-tenants']) 
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
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceSerializer, True).openapi}, tags=['admin-groups'])
        def get(self, request, *args, **kwargs):
            groups = self.get_queryset()
            serializer = self.serializer_class(groups, many=True)
            return success(serializer.data)
    
    class GetItensForGroupsView(generics.RetrieveAPIView):
        queryset = Items().get_defaults_items()
        serializer_class = ItemsSerializer
        lookup_field = 'code_group'
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ItemsSerializer, True).openapi}, tags=['admin-items'])
        def get(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            items = [item for item in queryset if item.code_group == kwargs.get(self.lookup_field)]
            if not items:
                raise Http404()
            serializer = self.serializer_class(items, many=True)
            return success(serializer.data)