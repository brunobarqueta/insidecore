from django.db import models
from simalfa.models.abstracts import ActiveBaseAbstract
from rest_framework import serializers

class Tenant(ActiveBaseAbstract):
    code = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=765, blank=False)

class TenantAllPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        exclude = ['active']
    
class TenantGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        exclude = ['id']