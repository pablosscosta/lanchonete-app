from django.db import models

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PREPARANDO', 'Preparando'),
        ('ENTREGUE', 'Entregue'),
        ('CANCELADO', 'Cancelado'),
    ]

    FORMA_PAGAMENTO_CHOICES = [
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO', 'Cartão'),
        ('PIX', 'Pix'),
    ]

    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    observacoes = models.TextField(blank=True)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
