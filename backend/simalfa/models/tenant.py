from django.db import models
from simalfa.models.abstracts import ActiveBaseAbstract
from rest_framework import serializers

class Tenant(ActiveBaseAbstract):
    code = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=765, blank=False)

    def alter_active_situation(self):
        self.active = not self.active

class TenantAllPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        exclude = ['active']
    
class TenantGetAlterDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        exclude = ['id']