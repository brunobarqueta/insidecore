from django.db import models
from rest_framework import serializers
from simalfa.models.tenant import Tenant, TenantAllPropertiesSerializer
from simalfa.models.abstracts import EntityCommonAbstract

class Formula(EntityCommonAbstract):
    description = models.CharField(max_length=255, blank=False)
    expression = models.CharField(max_length=4000, blank=False)
    tenants = models.ManyToManyField(Tenant, null=True, blank=True)
    
    def alter_active_situation(self):
        self.active = not self.active
    
class FormulaAllPropertiesSerializer(serializers.ModelSerializer):
    tenants = serializers.SerializerMethodField()
    class Meta:
        model = Formula
        fields = '__all__'
        
    def get_tenants(self, obj):
        tenant_instances = obj.tenants.all()
        return TenantAllPropertiesSerializer(tenant_instances, many=True).data

class FormulaListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        exclude = ['active']
    
class FormulaGetAlterDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        exclude = ['id']