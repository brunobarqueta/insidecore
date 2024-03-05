from rest_framework import generics
from tools_rest.response_view import success
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from simalfa.models.service import (Service, ServiceSerializer)
from simalfa.models.item import (Items, ItemsSerializer)
from simalfa.models.tenant import (Tenant, TenantAllPropertiesSerializer, TenantListCreateSerializer, TenantGetAlterDeleteSerializer)
from simalfa.models.metrics import (Metrics, MetricsAllPropertiesSerializer, MetricsListCreateSerializer, MetricsGetAlterDeleteSerializer)
from simalfa.models.formula import (Formula, FormulaAllPropertiesSerializer, FormulaListCreateSerializer, FormulaGetAlterDeleteSerializer)
from simalfa.models.serviceitem import (ServiceItem, ServiceItemAllPropertiesSerializer, ServiceItemListCreateSerializer, ServiceItemGetAlterDeleteSerializer)

# Create your views here.
class TenantCrudView:
    class TenantListCreateView(generics.ListCreateAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        def list(self, request, *args, **kwargs):

            queryset = self.filter_queryset(self.get_queryset())
            serializer = TenantAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        def post(self, request, *args, **kwargs):
            serializer = TenantAllPropertiesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
        
    class TenantGetAlterDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantGetAlterDeleteSerializer
        permission_classes = [IsAuthenticated]
            
        def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = TenantAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
    
        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = TenantAllPropertiesSerializer(instance)
            return success(serializer.data)

        def update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = TenantAllPropertiesSerializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return success(serializer.data)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return success(True)
        
class MetricsCrudView:
    class MetricsListCreateView(generics.ListCreateAPIView):
        queryset = Metrics.objects.all()
        serializer_class = MetricsListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = MetricsAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = MetricsAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class MetricsGetAlterDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Metrics.objects.all()
        serializer_class = MetricsGetAlterDeleteSerializer
        permission_classes = [IsAuthenticated]
            
        def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = MetricsAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
    
        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = MetricsAllPropertiesSerializer(instance)
            return success(serializer.data)

        def update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = MetricsAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return success(True)
        
class FormulaCrudView:
    class FormulaListCreateView(generics.ListCreateAPIView):
        queryset = Formula.objects.all()
        serializer_class = FormulaListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = FormulaAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = FormulaAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class FormulaGetAlterDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Formula.objects.all()
        serializer_class = FormulaGetAlterDeleteSerializer
        permission_classes = [IsAuthenticated]
            
        def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = FormulaAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
    
        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = FormulaAllPropertiesSerializer(instance)
            return success(serializer.data)

        def update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = FormulaAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return success(True)
        
class ServiceItemCrudView:
    class ServiceItemListCreateView(generics.ListCreateAPIView):
        queryset = ServiceItem.objects.all()
        serializer_class = ServiceItemListCreateSerializer
        permission_classes = [IsAuthenticated]
        
        def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            serializer = ServiceItemAllPropertiesSerializer(queryset, many=True)
            return success(serializer.data)
        
        def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                instance_serializer = ServiceItemAllPropertiesSerializer(instance)
                return success(instance_serializer.data)
        
    class ServiceItemGetAlterDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = ServiceItem.objects.all()
        serializer_class = ServiceItemGetAlterDeleteSerializer
        permission_classes = [IsAuthenticated]
            
        def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.alter_active_situation()
            
            serializer = ServiceItemAllPropertiesSerializer(instance, data=instance.__dict__, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return success(serializer.data)
    
        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = ServiceItemAllPropertiesSerializer(instance)
            return success(serializer.data)

        def update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                retorno = ServiceItemAllPropertiesSerializer(instance, data=request.data)
                retorno.is_valid(raise_exception=True)
                return success(retorno.data)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return success(True)

class ServicesCrudView:
    class GetGroupsView(generics.ListAPIView):
        queryset = Service().get_defaults_groups()
        serializer_class = ServiceSerializer
        permission_classes = [IsAuthenticated]
        
        def list(self, request, *args, **kwargs):
            groups = self.get_queryset()
            serializer = self.serializer_class(groups, many=True)
            return success(serializer.data)
    
    class GetItensForGroupsView(generics.ListAPIView):
        queryset = Items().get_defaults_items()
        serializer_class = ItemsSerializer
        lookup_field = 'code_group'
        permission_classes = [IsAuthenticated]
        
        def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            items = [item for item in queryset if item.code_group == kwargs.get(self.lookup_field)]
            serializer = self.serializer_class(items, many=True)
            return success(serializer.data)
            
        