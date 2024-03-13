from django.db import models
from rest_framework import serializers
from simalfa.models.abstracts import ActiveBaseAbstract
from simalfa.models.metrics import Metrics
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.metrics import Metrics, MetricsPropertiesSerializer

class ServiceItemMetrics(ActiveBaseAbstract):
    value = models.DecimalField(max_digits=25, decimal_places=5)
    tenant = models.ForeignKey(Tenant, null=True, blank=True, on_delete=models.CASCADE)
    metrics = models.ManyToManyField(Metrics, blank=True)
    
class ServiceItemMetricsAllPropertiesSerializer(serializers.ModelSerializer):
    tenant = serializers.SerializerMethodField()
    metrics = serializers.SerializerMethodField()
    class Meta:
        model = ServiceItemMetrics
        fields = '__all__'
    
    def get_tenant(self, obj):
        instance = obj.tenant
        if instance:
            return TenantAllPropertiesSerializer(instance).data
    
    def get_metrics(self, obj):
        instance = obj.metrics.all()
        return MetricsPropertiesSerializer(instance, many=True).data
         
class ServiceItemMetricsPropertiesSerializer(serializers.ModelSerializer):
    metrics = serializers.SerializerMethodField()
    class Meta:
        model = ServiceItemMetrics
        exclude = ['tenant']
    
    def get_metrics(self, obj):
        instance = obj.metrics.all()
        return MetricsPropertiesSerializer(instance, many=True).data

class ServiceItemMetricsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMetrics
        exclude = ['active']
    
class ServiceItemMetricsGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItemMetrics
        exclude = ['id']