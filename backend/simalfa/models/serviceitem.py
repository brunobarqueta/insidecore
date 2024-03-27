from django.db import models
from rest_framework import serializers
from simalfa.models.abstracts import EntityCommonAbstract
from simalfa.models.tenant import Tenant , TenantAllPropertiesSerializer
from simalfa.models.formula import Formula, FormulaPropertiesSerializer
from simalfa.models.serviceitemmetrcs import ServiceItemMetrics , ServiceItemMetricsPropertiesSerializer
import re

class ServiceItem(EntityCommonAbstract):
    code = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=765, blank=False)
    process = models.CharField(max_length=50, blank=False)
    rubric = models.CharField(max_length=4000, null=True, blank=True)
    application = models.CharField(max_length=4000, null=True, blank=True)
    service_item_metrics = models.ManyToManyField(ServiceItemMetrics, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    formula_fcl = models.ForeignKey(Formula, related_name='itens_servico_formula_fcl', on_delete=models.SET_NULL, null=True, blank=True)
    formula_lcl = models.ForeignKey(Formula, related_name='itens_servico_formula_lcl', on_delete=models.SET_NULL, null=True, blank=True)
    
class ServiceItemAllPropertiesSerializer(serializers.ModelSerializer):
    tenant = serializers.SerializerMethodField()
    service_item_metrics = serializers.SerializerMethodField()
    formula_fcl = serializers.SerializerMethodField()
    formula_lcl = serializers.SerializerMethodField()
    class Meta:
        model = ServiceItem
        fields = '__all__'
    
    def get_tenant(self, obj):
        instance = obj.tenant
        if instance:
            return TenantAllPropertiesSerializer(instance).data
    
    def get_service_item_metrics(self, obj):
        instance = obj.service_item_metrics.all()
        return ServiceItemMetricsPropertiesSerializer(instance, many=True).data
    
    def get_formula_fcl(self, obj):
        instance = obj.formula_fcl
        if instance:
            return FormulaPropertiesSerializer(instance).data
    
    def get_formula_lcl(self, obj):
        instance = obj.formula_lcl
        if instance:
            return FormulaPropertiesSerializer(instance).data

class ServiceItemMetricsUpdateerializer(serializers.Serializer):
    id_service_item_metric = serializers.IntegerField(required=True)
    id_metric = serializers.IntegerField(required=True)
    value = serializers.DecimalField(required=True, max_digits=25, decimal_places=5)

class ServiceItemGetAlterInputSerializer(serializers.ModelSerializer):
    metrics = ServiceItemMetricsUpdateerializer(many=True, required=False)
    class Meta:
        model = ServiceItem
        exclude = ['id', 'service_item_metrics']
    
    def validate(self, attrs):
        code_is_valid = re.match(r'^\d+(.\d+)*$', attrs['code'])
        if not code_is_valid:
            raise serializers.ValidationError({"code": "Código informado não é válido, Por favor, seguir o padrão 'x.x...'."})
        return attrs

class ServiceItemGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        exclude = ['id']
    
    def validate(self, attrs):
        code_is_valid = re.match(r'^\d+(.\d+)*$', attrs['code'])
        if not code_is_valid:
            raise serializers.ValidationError({"code": "Código informado não é válido, Por favor, seguir o padrão 'x.x...'."})
        return attrs

class ServiceItemMetricsCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    value = serializers.DecimalField(required=True, max_digits=25, decimal_places=5)

class ServiceItemCreateInputSerializer(serializers.ModelSerializer):
    metrics = ServiceItemMetricsCreateSerializer(many=True, required=False)
    class Meta:
        model = ServiceItem
        exclude = ['active', 'service_item_metrics']
        
    def validate(self, attrs):
        code_is_valid = re.match(r'^\d+(.\d{1,4}){1,3}$', attrs['code'])
        if not code_is_valid:
            raise serializers.ValidationError({"code": "Código informado não é válido, Por favor, seguir o padrão 'x.x...'."})
        return attrs
    
class ServiceItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        exclude = ['active']
        
    def validate(self, attrs):
        code_is_valid = re.match(r'^\d+(.\d{1,4}){1,3}$', attrs['code'])
        if not code_is_valid:
            raise serializers.ValidationError({"code": "Código informado não é válido, Por favor, seguir o padrão 'x.x...'."})
        return attrs