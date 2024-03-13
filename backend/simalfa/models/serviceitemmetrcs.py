from django.db import models
from rest_framework import serializers
from simalfa.models.abstracts import ActiveBaseAbstract
from simalfa.models.metrics import Metrics
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.metrics import Metrics, MetricsPropertiesSerializer

class ServiceItemMetrics(ActiveBaseAbstract):
    value = models.DecimalField(max_digits=25, decimal_places=5)
    tenant = models.ForeignKey(Tenant, null=True, blank=True, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metrics, null=True, blank=True, on_delete=models.CASCADE)
    
class ServiceItemMetricsAllPropertiesSerializer(serializers.ModelSerializer):
    tenant = serializers.SerializerMethodField()
    metric = serializers.SerializerMethodField()
    class Meta:
        model = ServiceItemMetrics
        fields = '__all__'
    
    def get_tenant(self, obj):
        instance = obj.tenant
        if instance:
            return TenantAllPropertiesSerializer(instance).data
    
    def get_metric(self, obj):
        instance = obj.metric
        if instance:
            return MetricsPropertiesSerializer(instance).data
         
class ServiceItemMetricsPropertiesSerializer(serializers.ModelSerializer):
    metric = serializers.SerializerMethodField()
    class Meta:
        model = ServiceItemMetrics
        exclude = ['tenant']
    
    def get_metric(self, obj):
        instance = obj.metric
        if instance:
            return MetricsPropertiesSerializer(instance).data

class ServiceItemMetricsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMetrics
        exclude = ['active']
    
class ServiceItemMetricsGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMetrics
        exclude = ['id']