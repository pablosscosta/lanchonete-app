from rest_framework import generics
from .models import Pedido
from .serializers import PedidoSerializer

class PedidoCreateAPIView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
