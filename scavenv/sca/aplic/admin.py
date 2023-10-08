from django.contrib import admin
from .models import Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')  # Campos exibidos na lista
    list_filter = ('categoria',)  # Filtros na lateral
    search_fields = ('nome', 'descricao')  # Campo de pesquisa