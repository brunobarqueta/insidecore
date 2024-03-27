from django.db import models
from rest_framework import serializers
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.metrics import Metrics, MetricsPropertiesSerializer
from simalfa.models.abstracts import EntityCommonAbstract

class Formula(EntityCommonAbstract):
    description = models.CharField(max_length=255, blank=False)
    expression = models.CharField(max_length=4000, blank=False)
    metrics = models.ManyToManyField(Metrics,blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
class FormulaAllPropertiesSerializer(serializers.ModelSerializer):
    tenant = serializers.SerializerMethodField()
    metrics = serializers.SerializerMethodField()
    class Meta:
        model = Formula
        fields = '__all__'
        
    def get_tenant(self, obj):
        tenant_instance = obj.tenant
        return TenantAllPropertiesSerializer(tenant_instance).data
        
    def get_metrics(self, obj):
        metric_instances = obj.metrics.all()
        return MetricsPropertiesSerializer(metric_instances, many=True).data

class FormulaPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        exclude = ['tenant', 'metrics']
        
    def get_metrics(self, obj):
        metric_instances = obj.metrics.all()
        return MetricsPropertiesSerializer(metric_instances, many=True).data

class FormulaListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        exclude = ['active']
    
class FormulaGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        exclude = ['id']