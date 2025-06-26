# usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Perfil

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class PerfilSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Perfil
        fields = ['id', 'user', 'telefone', 'cargo', 'ativo']
