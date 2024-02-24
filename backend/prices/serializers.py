from rest_framework import serializers
from .models import Price
from decimal import Decimal
from prices.tools import constantes
from prices.tools.validators import *

class PriceListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'
    
    def validate(self, attrs):
        if string_isnull_or_whitespace(attrs.get('name')):
           raise serializers.ValidationError(constantes.CAMPO_OBRIGATORIO.format('nome'))
       
        if  string_isnull_or_whitespace(attrs.get('description')):
           raise serializers.ValidationError(constantes.CAMPO_OBRIGATORIO.format('descricao'))
        
        price = attrs.get('price')
        if price is None:
            raise serializers.ValidationError(constantes.CAMPO_OBRIGATORIO.format('preco'))
        
        if not isinstance(price, Decimal):
            raise serializers.ValidationError(constantes.CAMPO_INVALIDO.format('preco', 'vazios'))
        
        if price < 0:
            raise serializers.ValidationError(constantes.CAMPO_INVALIDO.format('preco', 'negativos'))
        
        return attrs
    
    def create(self, validated_data):
        price = Price.objects.create(
            name = validated_data.get('name'), 
            description= validated_data.get('description'), 
            price= validated_data.get('price')
        )
        return price

class PriceGetPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ['id']

    def validate(self, attrs):
        name = attrs.get('name')
        if string_is_empty(name):
           raise serializers.ValidationError(constantes.CAMPO_INVALIDO.format('nome', 'vazios'))
       
        descricao = attrs.get('description')
        if string_is_empty(descricao):
           raise serializers.ValidationError(constantes.CAMPO_INVALIDO.format('descricao', 'vazios'))
        
        price = attrs.get('price')
        if price != None and not isinstance(price, Decimal):
           raise serializers.ValidationError(constantes.CAMPO_INVALIDO.format('price', 'vazios'))
        
        if price != None and price < 0:
            raise serializers.ValidationError(constantes.CAMPO_INVALIDO.format('preco', 'negativos'))
        
        if all_properies_nullables(name, descricao, price):
           raise serializers.ValidationError(constantes.ENTRADA_VAZIA)
            
        if name is None and descricao is None and price is None:
           raise serializers.ValidationError(constantes.ENTRADA_VAZIA)

        return attrs
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        
        instance.save()
        return instance

class PriceDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price