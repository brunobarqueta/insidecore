from django.db import models
from rest_framework import serializers
from simulation.models.metrics import MetricsEntity, MetricsAllPropertiesSerializer

class ServiceEntity(models.Model):
    code = models.CharField(max_length=4000, blank=False)
    items = models.ManyToManyField(MetricsEntity, blank=False)
    
class ServiceAllPropertiesSerializer(serializers.ModelSerializer):
    metrics = serializers.SerializerMethodField()
    class Meta:
        model = ServiceEntity
        fields = '__all__'
        
    def get_metrics(self, obj):
        instances = obj.items.all()
        return MetricsAllPropertiesSerializer(instances, many=True).data
