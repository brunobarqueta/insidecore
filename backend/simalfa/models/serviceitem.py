from django.db import models
from rest_framework import serializers
from simalfa.models.abstracts import EntityCommonAbstract
from simalfa.models.tenant import Tenant , TenantAllPropertiesSerializer
from simalfa.models.formula import Formula, FormulaAllPropertiesSerializer

class ServiceItem(EntityCommonAbstract):
    group_code = models.CharField(max_length=1, blank=False)
    item_code = models.CharField(max_length=1, blank=False)
    code = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=765, blank=False)
    process = models.CharField(max_length=50, blank=False)
    rubric = models.CharField(max_length=4000, blank=False)
    application = models.CharField(max_length=4000, blank=False)
    value = models.DecimalField(max_digits=25, decimal_places=5)
    tenants = models.ManyToManyField(Tenant, blank=True)
    formula_fcl = models.ForeignKey(Formula, related_name='itens_servico_formula_fcl', on_delete=models.SET_NULL, null=True, blank=True)
    formula_lcl = models.ForeignKey(Formula, related_name='itens_servico_formula_lcl', on_delete=models.SET_NULL, null=True, blank=True)
    
class ServiceItemAllPropertiesSerializer(serializers.Serializer):
    tenants = serializers.SerializerMethodField()
    formula_fcl = serializers.SerializerMethodField()
    formula_lcl = serializers.SerializerMethodField()
    
    def get_tenants(self, obj):
        intances = obj.tenants.all()
        return TenantAllPropertiesSerializer(intances, many=True).data
    
    def get_formula_fcl(self, obj):
        instante = obj.formula_fcl
        if instante:
            return FormulaAllPropertiesSerializer(instante).data
    
    def get_formula_lcl(self, obj):
        instante = obj.formula_lcl
        if instante:
            return FormulaAllPropertiesSerializer(instante).data
    
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