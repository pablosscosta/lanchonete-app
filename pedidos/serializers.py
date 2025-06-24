from rest_framework import serializers
from produtos.models import Produto
from .models import Pedido, ItemPedido

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade', 'preco_unitario']
    
class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)  # campo aninhado para múltiplos itens

    class Meta:
        model = Pedido
        fields = ['id', 'status', 'forma_pagamento', 'observacoes', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido

