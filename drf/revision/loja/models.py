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

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15)
    img = models.ImageField(upload_to = 'cliente/imagens')

    def __str__(self) -> str:
        return self.nome

class PedidoItem(models.Model): 
    produtos = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(null=False)

    def __str__(self) -> str:
        return str(self.id)

class Pedido(models.Model):
    STATUS_PAGO = 'P'
    STATUS_AGUARDANDO = 'A'
    STATUS_CANCELADO = 'C'

    STATUS_PG = [
        (STATUS_AGUARDANDO, 'Aguardando'),
        (STATUS_PAGO, 'Pago'),
        (STATUS_CANCELADO, 'Cancelado'),
    ]

    dt_pedido = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(max_length=1, choices=STATUS_PG, default='STATUS_AGUARDANDO')
    items = models.ManyToManyField(PedidoItem)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str(self.id)   

class Aval(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    dt_aval = models.DateField(auto_now_add=True)
    stars = models.PositiveSmallIntegerField()