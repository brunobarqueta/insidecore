from .models import CustomUser
from . import validators
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(error_messages={'invalid': 'Por favor, insira um endereço de e-mail válido.',})

    class Meta:
        model = CustomUser
        fields = ('email' ,'fullname', 'cpf', 'phone', 'password', 'password2')

    def validate(self, attrs):
        if not validators.validate_fullname(attrs['fullname']):
            raise serializers.ValidationError({"fullname": "Informe nome e sobrenome."})
        
        if not validators.validate_cpf_mask(attrs['cpf']):
            raise serializers.ValidationError({"cpf": "Cpf está no formato inválido."})
        
        if not validators.validate_phone(attrs['phone']):
            raise serializers.ValidationError({"phone": "Numero de telefone é inválido."})
            
        if not validators.validate_cpf(attrs['cpf']):
            raise serializers.ValidationError({"cpf": "Cpf informado é inválido"})
            
        if not validators.validate_passwords(attrs['password'], attrs['password2']):
            raise serializers.ValidationError(
                {"password2": "Senhas informadas são diferentes."})
        
        return attrs

    def create(self, validated_data):
        fullname = str(validated_data['fullname']).title()
        phone = re.sub(r'[^\d]','',validated_data['phone'])
        
        split_name = fullname.split()
        first_name = split_name[0]
        last_name = split_name[-1]
        
        try:
            user = CustomUser.objects.create(
                email=validated_data['email'],
                cpf=validated_data['cpf'],
                fullname=fullname,
                phone=phone,
                first_name=first_name,
                last_name=last_name
            )
        except:
            raise serializers.ValidationError({"Erro": "Erro ao cadastrar usuario."})
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user
