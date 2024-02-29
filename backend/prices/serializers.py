from rest_framework import serializers
from .models import Price

class PriceListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'
    

class PriceGetPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        exclude = ['id']


class PriceDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price