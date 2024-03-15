from rest_framework import serializers
from simulation.enums import TypeService

#class GetFilterServiceItemSerializer(serializers.ModelSerializer):
class GetFilterServiceItemSerializer(serializers.Serializer):
    type_service = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TypeService])

class DescriptionSerializer(serializers.Serializer):
    code = serializers.CharField()
    description = serializers.CharField()

class ServiceItemOutputSerializer(serializers.Serializer):
    service = serializers.CharField()
    description = serializers.SerializerMethodField()
    
    def get_description(self, obj):
        for item in self.initial_data:
            if item.get('service') == obj.get('service'):
                return DescriptionSerializer(item.get('description', []), many=True).data