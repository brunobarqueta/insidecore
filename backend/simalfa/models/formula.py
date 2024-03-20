from django.db import models
from rest_framework import serializers
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.metrics import Metrics, MetricsPropertiesSerializer
from simalfa.models.abstracts import EntityCommonAbstract

class Formula(EntityCommonAbstract):
    description = models.CharField(max_length=255, blank=False)
    expression = models.CharField(max_length=4000, blank=False)
    metrics = models.ManyToManyField(Metrics,blank=True)
    tenants = models.ManyToManyField(Tenant,blank=True)
    
class FormulaAllPropertiesSerializer(serializers.ModelSerializer):
    tenants = serializers.SerializerMethodField()
    metrics = serializers.SerializerMethodField()
    class Meta:
        model = Formula
        fields = '__all__'
        
    def get_tenants(self, obj):
        tenant_instances = obj.tenants.all()
        return TenantAllPropertiesSerializer(tenant_instances, many=True).data
        
    def get_metrics(self, obj):
        metric_instances = obj.metrics.all()
        return MetricsPropertiesSerializer(metric_instances, many=True).data

class FormulaPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        exclude = ['tenants', 'metrics']
        
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