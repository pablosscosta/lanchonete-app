from django.urls import path
from .views import PedidoCreateAPIView

urlpatterns = [
    path('api/pedidos/', PedidoCreateAPIView.as_view(), name='pedido-create'),
]
