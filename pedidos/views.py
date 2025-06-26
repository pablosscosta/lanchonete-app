from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pedido, ItemPedido
from .serializers import PedidoSerializer, ItemPedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'usuarios']
    ordering_fields = ['criado_em']

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
