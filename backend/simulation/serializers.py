from rest_framework import serializers
from simulation.enums import TypeService
from simalfa.models.serviceitemmetrcs import ServiceItemMetricsPropertiesSerializer
from logins import validators
import re, decimal

#class GetFilterServiceItemSerializer(serializers.ModelSerializer):
class GetFilterServiceItemSerializer(serializers.Serializer):
    type_service = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TypeService])

class DescriptionSerializer(serializers.Serializer):
    code = serializers.CharField()
    description = serializers.CharField()
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

class ServiceItemMetricsInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    value = serializers.DecimalField(max_digits=25, decimal_places=5, required=False)
     
class ServiceItemInputSerializer(serializers.Serializer):
    code = serializers.CharField(required=False)
    metrics = ServiceItemMetricsInputSerializer(many=True, required=False)
    
class DataServiceInputSerializer(serializers.Serializer):
    type_service = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TypeService])
    company = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    telephone = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    date_arrival = serializers.DateTimeField(required=False, allow_null=True)
    date_exit = serializers.DateTimeField(required=False, allow_null=True)
    services = ServiceItemInputSerializer(many=True)
    
    def to_internal_value(self, data):
        # Remove validators for the 'value' field
        if 'value' in data:
            data['value'] = self.fields['value'].to_internal_value(data['value'])
        return data
    
    def validate(self, attrs):
        if not validators.validate_fullname(attrs['name']):
            raise serializers.ValidationError("Informe nome e sobrenome.")
        
        if not validators.validate_phone(attrs['telephone']):
            raise serializers.ValidationError("Numero de telefone é inválido.")
        
        services = attrs.get('services', None)
        if not services:
            raise serializers.ValidationError("Nenhum serviço foi selecionado")
        
        for service in services:
            code = service.get('code', '')
            code_is_valid = re.match(r'^\d+(.\d+)*$', code)
            if not code_is_valid:
                raise serializers.ValidationError(f"Código '{code}' não é válido, Por favor, seguir o padrão 'x.x...'.")

            metrics = service.get('metrics', [])
            for metric in metrics:
                id = metric.get('id', 0)
                value = metric.get('value')
                
                if id <= 0:
                    raise serializers.ValidationError(f"Id '{id}' não é válido.")
                
                try: decimal.Decimal(value)
                except: raise serializers.ValidationError(f"Valor '{value}' não é válido.")
                
        return attrs
    
class OutputModels:
    class ItemSimulationOutputSerializer(serializers.Serializer):
        code = serializers.CharField(required=True)
        amount = serializers.DecimalField(max_digits=25, decimal_places=5, required=True)
        unity = serializers.CharField(required=True)
        description = serializers.CharField(required=True)
        value = serializers.CharField(required=True)
    
    class ServicesSimulatrionOutputSerializer(serializers.Serializer):
        service = serializers.CharField(required=True)
        total = serializers.CharField(required=True)
        items = serializers.SerializerMethodField()
        
        def get_items(self, obj):
            services = obj.get('items', [])
            tt = OutputModels.ItemSimulationOutputSerializer(services, many=True).data
            return tt
    
    class DataClientSimulationOutputSerializer(serializers.Serializer):
        type_service = serializers.CharField(required=True)
        name = serializers.CharField(required=True)
        company = serializers.CharField(required=True)
        auto_number = serializers.CharField(required=True)
        date_register = serializers.DateTimeField(required=True)
        email = serializers.EmailField(required=True)
        cif = serializers.CharField(required=True)
        total = serializers.CharField(required=True)
        services = serializers.SerializerMethodField()
        
        def get_services(self, obj):
            services = obj.get('services', [])
            tt = OutputModels.ServicesSimulatrionOutputSerializer(services, many=True).data
            return tt

    