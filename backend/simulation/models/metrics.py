from django.db import models
from rest_framework import serializers
from simalfa.models.metrics import Metrics

class MetricsEntity(models.Model):
    id_metric = models.ForeignKey(Metrics, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=15, decimal_places=5, blank=False)
    
class MetricsAllPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricsEntity
        fields = '__all__'