from django.db import models
from rest_framework import serializers
from abstracts import EntityCommonAbstract
from models.tenant import Tenant , TenantAllPropertiesSerializer
from models.formula import Formula, FormulaAllPropertiesSerializer

class ServiceItem(EntityCommonAbstract):
    code = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=765, blank=False)
    process = models.CharField(max_length=50, blank=False)
    rubric = models.CharField(max_length=4000, blank=False)
    application = models.CharField(max_length=4000, blank=False)
    tenants = models.ManyToManyField(Tenant, blank=True)
    formulas = models.ManyToManyField(Formula, blank=True)
    
class ServiceItemAllPropertiesSerializer(serializers.Serializer):
    tenants = serializers.SerializerMethodField()
    formulas = serializers.SerializerMethodField()
    
    def get_tenants(self, obj):
        intances = obj.tenants.all()
        return TenantAllPropertiesSerializer(intances, many=True).data
    
    def get_formulas(self, obj):
        instantes = obj.formulas.all()
        return FormulaAllPropertiesSerializer(instantes, many=True).data
    
    class Meta:
        models = ServiceItem
        fields = '__all__'
        
class ServiceItemListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        exclude = ['active']
    
class ServiceItemGetAlterDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        exclude = ['id']