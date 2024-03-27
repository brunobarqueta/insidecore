from django.db import models
from rest_framework import serializers
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.abstracts import EntityCommonAbstract
from simalfa.enums import TypeMetric

TYPE_CHOICES = [(tag.value, tag.value) for tag in TypeMetric]
class Metrics(EntityCommonAbstract):
    description = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, blank=False)
    service = models.CharField(max_length=4000, blank=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
class MetricsAllPropertiesSerializer(serializers.ModelSerializer):
    tenant = serializers.SerializerMethodField()
    class Meta:
        model = Metrics
        fields = '__all__'
        
    def get_tenant(self, obj):
        tenant_instance = obj.tenant
        return TenantAllPropertiesSerializer(tenant_instance).data

class MetricsPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['tenant']

class MetricsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['active']
    
class MetricsGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['id']