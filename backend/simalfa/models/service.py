from rest_framework import serializers

class Service():
    def __init__(self, code:int = None, name:str = None):
        self.code = code
        self.name = name
    
    @staticmethod
    def get_defaults_groups():
        groups = []
        groups.append(Service(1, 'Serviços Inerentes'))
        groups.append(Service(2, 'Serviços Complementares'))
        groups.append(Service(3, 'Serviços Acessórios'))
        return groups
    
class ServiceSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        fields = ['code', 'name']