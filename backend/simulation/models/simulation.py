from django.db import models
from rest_framework import serializers
from simalfa.models import tenant
from simulation.models.service import ServiceEntity, ServiceAllPropertiesSerializer
from simulation.enums import TypeService
from datetime import datetime

class SimulationEntity(models.Model):
    type_service = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in TypeService], blank=False)
    auto_number = models.DecimalField(max_digits=100, decimal_places=0, unique=True, blank=True)
    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    cif = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    date_arrival = models.DateTimeField(null=True, blank=True)
    date_exit = models.DateTimeField(null=True, blank=True)
    services = models.ManyToManyField(ServiceEntity, blank=False)
    tenant = models.ForeignKey(tenant.Tenant, on_delete=models.CASCADE)
    date_register = models.DateTimeField(default=datetime.now)
    
class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationEntity
        fields = '__all__'

class SimulationGetSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()
    tenant = serializers.SerializerMethodField()
    class Meta:
        model = SimulationEntity
        fields = '__all__'
        
    def get_tenant(self, obj):
        instance = obj.tenant
        return tenant.TenantAllPropertiesSerializer(instance).data
    
    def get_services(self, obj):
        instances = obj.services.all()
        return ServiceAllPropertiesSerializer(instances, many=True).data