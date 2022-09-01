from rest_framework import serializers
from .models import Produto, Pedido, PedidoItem, Cliente
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
        fields = ("id", "produtos", "quantidade")

class PedidoSerializer(serializers.ModelSerializer):
    kk = ItemSerializer(many=True, source="kk")
    class Meta:
        model = Pedido
        fields = ("id", "dt_pedido", "status_pagamento", "kk", "cliente")