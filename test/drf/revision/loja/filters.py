from django_filters.rest_framework import FilterSet
from .models import Produto

class ProdutoFiltro(FilterSet):
    class Meta:
        model = Produto
        fields = {
            'categoria': ['exact'],
            'preco': ['gt', 'lt'],
        }