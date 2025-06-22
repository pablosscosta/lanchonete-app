from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'ativo', 'telefone')
    list_filter = ('cargo', 'ativo')
    search_fields = ('user__username', 'user__email', 'telefone')
