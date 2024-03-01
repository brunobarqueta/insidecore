from django.db import models
from rest_framework import serializers
from models.abstracts import EntityCommonAbstract
from models.metrics import Metrics
from backend.simalfa.models.serviceitem import ServiceItem
from models.tenant import Tenant, TenantAllPropertiesSerializer
from models.metrics import Metrics, MetricsAllPropertiesSerializer

class ServiceItemMetrics(EntityCommonAbstract):
    value = models.DecimalField(max_digits=25, decimal_places=5)
    service_item = models.ManyToManyField(ServiceItem,blank=False)
    tenants = models.ManyToManyField(Tenant,blank=True)
    metrics = models.ManyToManyField(Metrics)
    
class ServiceItemMetricsAllPropertiesSerializer(serializers.Serializer):
    tenants = serializers.SerializerMethodField()
    metrics = serializers.SerializerMethodField()
    
    def get_tenants(self, obj):
        tenant_instances = obj.tenants.all()
        return TenantAllPropertiesSerializer(tenant_instances, many=True).data
    
    def get_metrics(self, obj):
        tenant_instances = obj.metrics.all()
        return MetricsAllPropertiesSerializer(tenant_instances, many=True).data
    
    class Meta:
        models = ServiceItemMetrics
        fields = '__all__'
        
class ServiceItemMetricsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMetrics
        exclude = ['active']
    
class ServiceItemMetricsGetAlterDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMetrics
        exclude = ['id']