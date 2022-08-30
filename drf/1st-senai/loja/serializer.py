from unicodedata import category
from rest_framework import serializers
from .models import Produto
from decimal import Decimal

class ProdAdd(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'title', 'price', 'price_tax', 'stock', 'desc', 'category']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)

    price_tax = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self, produto : Produto):
        return produto['price'] * Decimal(1.1)
        
