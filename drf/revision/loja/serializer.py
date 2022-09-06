from rest_framework import serializers
from .models import Aval, Produto, Pedido, PedidoItem, Cliente
from decimal import Decimal

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','titulo','preco','preco_taxado', 'qtd_estoque', 'categoria']
    
    #10% de acréscimo
    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self, produto : Produto):
        return produto.preco * Decimal(1.1)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'cpf')
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = ("produtos", "quantidade")

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('__all__')

class AvalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aval
        fields = ('__all__')