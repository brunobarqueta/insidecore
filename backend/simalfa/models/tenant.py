from django.db import models
from simalfa.models.abstracts import ActiveBaseAbstract
from rest_framework import serializers
import uuid

class Tenant(ActiveBaseAbstract):
    code = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=765, blank=False)
    guid = models.CharField(default=uuid.uuid4, max_length=36, unique=True)

class TenantAllPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        exclude = ['active', 'guid']
    
class TenantGetAlterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        exclude = ['id', 'guid', 'active']