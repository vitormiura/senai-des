from rest_framework import serializers
from .models import Produto
from decimal import Decimal

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','titulo','preco','preco_taxado', 'qtd_estoque', 'categoria']
    
    #10% de acréscimo
    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self, produto : Produto):
        return produto.preco * Decimal(1.1)

