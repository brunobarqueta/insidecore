from django.db import models
from rest_framework import serializers
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.abstracts import EntityCommonAbstract

class Metrics(EntityCommonAbstract):
    description = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=50)
    service = models.CharField(max_length=4000, blank=False)
    tenants = models.ManyToManyField(Tenant, blank=True)
    
class MetricsAllPropertiesSerializer(serializers.ModelSerializer):
    tenants = serializers.SerializerMethodField()
    class Meta:
        model = Metrics
        fields = '__all__'
        
    def get_tenants(self, obj):
        tenant_instances = obj.tenants.all()
        return TenantAllPropertiesSerializer(tenant_instances, many=True).data

class MetricsPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['tenants']

class MetricsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['active']
    
class MetricsGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['id']