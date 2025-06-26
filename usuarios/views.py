from rest_framework import viewsets
from .models import Perfil
from django.contrib.auth.models import User
from .serializers import UserSerializer, PerfilSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
