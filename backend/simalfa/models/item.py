from rest_framework import serializers

class Items:
    def __init__(self, code_group:int = None, code:int = None, description:str = None):
        self.code_group = code_group
        self.code = code
        self.description = description
    
    @staticmethod
    def get_defaults_items():
        itens = []
        itens.append(Items(1, 1, 'Cais'))
        itens.append(Items(1, 2, 'Pátio'))
        itens.append(Items(2, 1, 'Armazenagem'))
        itens.append(Items(2, 2, 'Outros'))
        itens.append(Items(3, 1, 'Estufagem ou desestufagem, por contêiner'))
        itens.append(Items(3, 2, 'Fornecimento de fotografias digitais, por conjunto de 05 (cinco) fotos'))
        itens.append(Items(3, 3, 'Permanência de veículos no pátio interno, após a conclusão da operação, por veículo e por hora e fração'))
        itens.append(Items(3, 4, 'Limpeza do tanque de contenção e destinação de resíduos, por tanque'))
        itens.append(Items(3, 5, 'Fornecimento de água potável para embarcações, por m³'))
        itens.append(Items(3, 6, 'Fornecimento de energia elétrica para embarcações, por KWh'))
        itens.append(Items(3, 7, 'Limpeza de contêiner, por contêiner'))
        itens.append(Items(3, 8, 'Repesagem de carga, por contêiner.'))
        itens.append(Items(3, 9, 'Enlonamento, por contêiner'))
        itens.append(Items(3, 10, 'Fumigação, por contêine'))
        return itens
    
class ItemsSerializer(serializers.Serializer):
    code_group = serializers.IntegerField()
    code = serializers.IntegerField()
    description = serializers.CharField()

    class Meta:
        fields = '__all__'