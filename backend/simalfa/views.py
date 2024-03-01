from rest_framework import generics
from tools_rest.response_view import success
from simalfa.models.tenant import (Tenant, TenantAllPropertiesSerializer, TenantListCreateSerializer, TenantGetAlterDeleteSerializer)
from simalfa.models.metrics import (Metrics, MetricsAllPropertiesSerializer, MetricsListCreateSerializer, MetricsGetAlterDeleteSerializer)
from simalfa.models.formula import (Formula, FormulaAllPropertiesSerializer, FormulaListCreateSerializer, FormulaGetAlterDeleteSerializer)
#from simalfa.models.serviceitem import *
#from simalfa.models.serviceitemmetrcs import *

# Create your views here.
class TenantCrudView:
    class TenantListCreateView(generics.ListCreateAPIView):
        queryset = Tenant.objects.all()
        serializer_class = TenantListCreateSerializer
        
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