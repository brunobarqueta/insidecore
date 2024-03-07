from django.db import models
from rest_framework import serializers
from simalfa.models.abstracts import EntityCommonAbstract
from simalfa.models.tenant import Tenant , TenantAllPropertiesSerializer
from simalfa.models.formula import Formula, FormulaAllPropertiesSerializer
from simalfa.models.serviceitemmetrcs import ServiceItemMetrics , ServiceItemMetricsAllPropertiesSerializer

class ServiceItem(EntityCommonAbstract):
    code = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=765, blank=False)
    process = models.CharField(max_length=50, blank=False)
    rubric = models.CharField(max_length=4000, null=True, blank=True)
    application = models.CharField(max_length=4000, null=True, blank=True)
    tenants = models.ManyToManyField(Tenant, blank=True)
    metrics = models.ManyToManyField(ServiceItemMetrics, blank=True)
    formula_fcl = models.ForeignKey(Formula, related_name='itens_servico_formula_fcl', on_delete=models.SET_NULL, null=True, blank=True)
    formula_lcl = models.ForeignKey(Formula, related_name='itens_servico_formula_lcl', on_delete=models.SET_NULL, null=True, blank=True)
    
class ServiceItemAllPropertiesSerializer(serializers.ModelSerializer):
    tenants = serializers.SerializerMethodField()
    metrics = serializers.SerializerMethodField()
    formula_fcl = serializers.SerializerMethodField()
    formula_lcl = serializers.SerializerMethodField()
    metrics = serializers.SerializerMethodField()
    class Meta:
        model = ServiceItem
        fields = '__all__'
    
    def get_tenants(self, obj):
        intances = obj.tenants.all()
        return TenantAllPropertiesSerializer(intances, many=True).data
    
    def get_metrics(self, obj):
        intances = obj.metrics.all()
        return ServiceItemMetricsAllPropertiesSerializer(intances, many=True).data
    
    def get_formula_fcl(self, obj):
        instance = obj.formula_fcl
        if instance:
            return FormulaAllPropertiesSerializer(instance).data
    
    def get_formula_lcl(self, obj):
        instance = obj.formula_lcl
        if instance:
            return FormulaAllPropertiesSerializer(instance).data
    
class ServiceItemListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        exclude = ['active']
    
class ServiceItemGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        exclude = ['id']