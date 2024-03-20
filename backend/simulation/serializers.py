from rest_framework import serializers
from simulation.enums import TypeService
from simalfa.models.serviceitemmetrcs import ServiceItemMetricsPropertiesSerializer, ServiceItemMetrics

#class GetFilterServiceItemSerializer(serializers.ModelSerializer):
class GetFilterServiceItemSerializer(serializers.Serializer):
    type_service = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TypeService])

class DescriptionSerializer(serializers.Serializer):
    code = serializers.CharField()
    description = serializers.CharField()
    expression = serializers.CharField()
    metrics = serializers.SerializerMethodField()

    def get_metrics(self, obj):
        service_item_metrics = ServiceItemMetricsPropertiesSerializer(obj.get('metrics', {}), many=True).data
        result = []
        for metric_item in service_item_metrics:
            metric = metric_item.get('metric', {})
            if metric_item.get('active', False) and metric.get('active', False):
                result.append({
                    'description': metric['description'], 
                    'type': metric['type'],
                    'service': metric['service'],
                    'value': metric_item['value']
                })
        
        return result

class ServiceItemOutputSerializer(serializers.Serializer):
    service = serializers.CharField()
    items = serializers.ListField()
    
    def get_items(self, obj):
        for item in self.initial_data:
            if item.get('service') == obj.get('service'):
                return DescriptionSerializer(item.get('items', []), many=True).data
            
class ServiceItemInputSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)
    
class DataServiceInputSerializer(serializers.Serializer):
    type_service = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TypeService])
    company = serializers.CharField(required=True)
    client_name = serializers.CharField(required=True)
    telephone = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    cif = serializers.DecimalField(max_digits=25, decimal_places=5, required=True)
    data_entrada = serializers.DateTimeField(required=False, allow_null=True)
    data_saida = serializers.DateTimeField(required=False, allow_null=True)
    services = ServiceItemInputSerializer(many=True)
    
    
    