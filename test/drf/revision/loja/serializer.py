from rest_framework import serializers
from .models import Aval, Produto, Pedido, PedidoItem, Cliente, Categoria
from decimal import Decimal

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','titulo','preco','preco_taxado', 'qtd_estoque', 'categoria']
    
    #10% de acréscimo
    preco_taxado = serializers.SerializerMethodField(method_name='calcular_taxa')

    def create(self, validated_data):
        if self.validated_data['qtd_estoque'] < 0:
            validated_data['qtd_estoque'] = 0
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if self.validated_data['qtd_estoque'] < 0:
            validated_data['qtd_estoque'] = 0
        return super().update(instance, validated_data)

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
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('__all__')

class AvalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aval
        fields = ('__all__')