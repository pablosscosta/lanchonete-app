from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
        ('LANCHES', 'Lanches'),
        ('BEBIDAS', 'Bebidas'),
        ('PORCOES', 'Porções'),
        ('SOBREMESAS', 'Sobremesas'),
        ('ADICIONAIS', 'Adicionais'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.nome

