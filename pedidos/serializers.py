from rest_framework import serializers
from .models import Pedido, ItemPedido
from produtos.serializers import ProdutoSerializer  # se quiser detalhar o produto no item

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)  # para mostrar dados do produto no GET
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Pedido.objects.all(), source='produto', write_only=True
    )

    class Meta:
        model = ItemPedido
        fields = ['id', 'produto', 'produto_id', 'quantidade', 'preco_unitario']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)
    usuarios = serializers.StringRelatedField()  # mostra o username no GET

    class Meta:
        model = Pedido
        fields = ['id', 'usuarios', 'data_hora', 'status', 'observacoes', 'forma_pagamento', 'total', 'criado_em', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        for item_data in itens_data:
            ItemPedido.objects.create(pedido=pedido, **item_data)
        return pedido
