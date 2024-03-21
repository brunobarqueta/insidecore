from rest_framework import generics
from tools_rest.response_view import success, bad_request
from tools_rest.swagger_view import SwaggerResultViewModel
from rest_framework.permissions import IsAuthenticated
from simalfa.models.tenant import (Tenant, TenantAllPropertiesSerializer, TenantListCreateSerializer, TenantGetAlterSerializer)
from simalfa.models.metrics import (Metrics, MetricsAllPropertiesSerializer, MetricsListCreateSerializer, MetricsGetAlterSerializer, MetricsPropertiesSerializer)
from simalfa.models.formula import (Formula, FormulaAllPropertiesSerializer, FormulaListCreateSerializer, FormulaGetAlterSerializer, FormulaPropertiesSerializer)
from simalfa.models.serviceitem import (ServiceItem, ServiceItemAllPropertiesSerializer, ServiceItemCreateInputSerializer, ServiceItemCreateSerializer, ServiceItemGetAlterSerializer, ServiceItemGetAlterInputSerializer)
from simalfa.models.serviceitemmetrcs import (ServiceItemMetrics, ServiceItemMetricsListCreateSerializer, ServiceItemMetricsPropertiesSerializer)
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
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, True, methodField=
        {
            'tenants': (True, TenantAllPropertiesSerializer),
            'metrics': (True, MetricsPropertiesSerializer)
        }).openapi}, tags=['admin-formulas'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = FormulaAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField=
        {
            'tenants': (True, TenantAllPropertiesSerializer),
            'metrics': (True, MetricsPropertiesSerializer)
        }).openapi}, tags=['admin-formulas'])
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
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField=
        {
            'tenants': (True, TenantAllPropertiesSerializer),
            'metrics': (True, MetricsPropertiesSerializer)
        }).openapi}, tags=['admin-formulas'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = FormulaAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=FormulaGetAlterSerializer,responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField=
        {
            'tenants': (True, TenantAllPropertiesSerializer),
            'metrics': (True, MetricsPropertiesSerializer)
        }).openapi}, tags=['admin-formulas'])
        def put(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = FormulaAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(FormulaAllPropertiesSerializer, methodField=
        {
            'tenants': (True, TenantAllPropertiesSerializer),
            'metrics': (True, MetricsPropertiesSerializer)
        }).openapi}, tags=['admin-formulas'])
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
        serializer_class = ServiceItemCreateInputSerializer
        permission_classes = [IsAuthenticated]
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenant': (False, TenantAllPropertiesSerializer),
                'service_item_metrics': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def get(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = ServiceItemAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenant': (False, TenantAllPropertiesSerializer),
                'service_item_metrics': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def post(self, request, *args, **kwargs):
            serializer = ServiceItemCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            if ServiceItem.objects.filter(code=request.data.get('code')).exists():
                return bad_request('Código informado ja é utilizado')
            
            metrics = []
            for metric in request.data.get('metrics'):
                id_metric = metric.get('id', None)
                try:
                    metric_instance = Metrics.objects.get(pk=id_metric)
                except:
                    return bad_request(f'Metrica de identificador {id_metric} não encontrada.')
                
                data = {
                    'value': metric.get('value', '0'),
                    'metric': metric_instance.id,
                    'tenant': request.data.get('tenant', None)
                }
                metrics.append(data)
            
            ids_service_item_metrics = []
            for metric_data in metrics:
                serializer = ServiceItemMetricsListCreateSerializer(data=metric_data)
                serializer.is_valid(raise_exception=True)
                item = serializer.save()
                ids_service_item_metrics.append(item.id)
            
            request.data['service_item_metrics'] = ids_service_item_metrics
            serializer = ServiceItemCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = ServiceItemAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class ServiceItemGetAlterView(generics.RetrieveUpdateAPIView):
        queryset = ServiceItem.objects.all()
        serializer_class = ServiceItemGetAlterInputSerializer
        permission_classes = [IsAuthenticated]
            
        def get_serializer_class(self):
            if self.request.method in ['GET', 'PATCH']:
                return None
            else:
                return ServiceItemGetAlterSerializer
    
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenant': (False, TenantAllPropertiesSerializer),
                'service_item_metrics': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def get(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = ServiceItemAllPropertiesSerializer(instance)
            return success(serializer.data)

        @swagger_auto_schema(request_body=ServiceItemGetAlterInputSerializer, responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenant': (False, TenantAllPropertiesSerializer),
                'service_item_metrics': (True, ServiceItemMetricsPropertiesSerializer),
                'formula_fcl':(False, FormulaPropertiesSerializer), 
                'formula_lcl':(False, FormulaPropertiesSerializer)
            }).openapi}, tags=['admin-service-items'])
        def put(self, request, *args, **kwargs):
            serializer = ServiceItemGetAlterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            instance = self.get_object()
            code = request.data['code']
            if instance.code != code and ServiceItem.objects.filter(code=code):
                return bad_request(f"Código '{code}' ja esta sendo utilizado.")
            
            serializer_list = []
            for metric in request.data.get('metrics'):
                id_item_service_metric = metric.get('id_service_item_metric', None)
                id_metric = metric.get('id_metric', None)
                value = metric.get('value', '0')
                
                try:
                    if id_item_service_metric == 0:
                        service_metrics = ServiceItemMetrics(value=value)
                        service_metrics.save()
                    else:
                        service_metrics = instance.service_item_metrics.get(pk=id_item_service_metric)
                except:
                    return bad_request(f'Metrica do item serviço de identificador {id_item_service_metric} não encontrada.')
                
                data = {
                    'value': value,
                    'metric': id_metric,
                    'tenant': request.data.get('tenant', instance.tenant)
                }
                serializer = ServiceItemMetricsListCreateSerializer(service_metrics, data=data)
                serializer.is_valid(raise_exception=True)
                serializer_list.append(serializer)
            
            ids_service_item_metrics = []
            for serializer_item in serializer_list:
                serializer_item.save()
                ids_service_item_metrics.append(serializer_item.data['id'])
                
            request.data['service_item_metrics'] = ids_service_item_metrics
            serializer = ServiceItemGetAlterSerializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = ServiceItemAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)
            
        @swagger_auto_schema(responses={200: SwaggerResultViewModel(ServiceItemAllPropertiesSerializer, True, 
            {
                'tenant': (False, TenantAllPropertiesSerializer),
                'service_item_metrics': (True, ServiceItemMetricsPropertiesSerializer),
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