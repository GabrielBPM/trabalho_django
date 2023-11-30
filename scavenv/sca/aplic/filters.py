# filters.py
import django_filters
from .models import Produto

class ProdutoFilter(django_filters.FilterSet):
    shampoo = django_filters.BooleanFilter(field_name='shampoo', label='Shampoo'),
    condicionador = django_filters.BooleanFilter(field_name='condicionador', label='Condicionador')

class ProdutoFilter(django_filters.FilterSet):
    class Meta:
        model = Produto
        fields = {
            'shampoo': ['exact'],
            'condicionador': ['exact'],
            # Outros campos de filtro, se houver
        }
