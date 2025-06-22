from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    CARGO_CHOICES = [
        ('ATENDENTE', 'Atendente'),
        ('GERENTE', 'Gerente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
