from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.categoria

class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descritivo = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_estoque = models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo

class Pedido(models.Model):

    STATUS_PG = [

    ]
    dt_pedido = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(max_length=1, choices=STATUS_PG, default='')
    
#class Pedido e PedidoItem