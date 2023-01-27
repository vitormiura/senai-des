from audioop import maxpp
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    descritivo = models.TextField()
    qtd_estoque = models.IntegerField()
    titulo = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

class Cliente(models.Model):
    CLIENTE_FREE = 'F'
    CLIENTE_PREMIUM = 'P'
    CLIENTE_DIAMOND = 'D'
    
    TIPOS_PLANOS = [
        (CLIENTE_FREE, 'Free'),
        (CLIENTE_PREMIUM, 'Premium'),
        (CLIENTE_DIAMOND, 'Diamond'),
    ]

    cpf = models.IntegerField()
    tipo = models.CharField(
        max_length = 1,
        choices = TIPOS_PLANOS,
        default = CLIENTE_FREE
        )
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=20)
    dt_cadastro = models.DateField(auto_created=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=8)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length = 50)
    cep = models.CharField(max_length = 8)
    cliente = models.ForeignKey(Cliente, on_delete= models.PROTECT)

#CRIAR MODELOS PEDIDO E PEDIDOITEM

class Pedido(models.Model):
    STATUS_PAGAMENTO_PAGO = 'P'
    STATUS_PAGAMENTO_AGUARDO = 'A'
    STATUS_PAGAMENTO_CANCELADO = 'C'
    STATUS_PAGAMENTO_NAO_PAGO = 'N'

    TIPOS_STATUS_PAGAMENTO = [
        (STATUS_PAGAMENTO_PAGO,'Pago'),
        (STATUS_PAGAMENTO_AGUARDO,'Aguardo'),
        (STATUS_PAGAMENTO_CANCELADO,'Cancelado'),
        (STATUS_PAGAMENTO_NAO_PAGO,'Nao Pago'),
    ]

# //////////////////////////////////////////////////////////////////////////////////////////

    STATUS_PEDIDO_ENTREGUE = 'E'
    STATUS_PEDIDO_TRANSPORTE = 'T'
    STATUS_PEDIDO_ESTOQUE = 'C'
    STATUS_PEDIDO_AGUARDANDO = 'A'

    TIPOS_STATUS_PEDIDO = [
        (STATUS_PEDIDO_ENTREGUE, 'Entregue'),
        (STATUS_PEDIDO_TRANSPORTE, 'Transporte'),
        (STATUS_PEDIDO_ESTOQUE, 'Cancelado'),
        (STATUS_PEDIDO_AGUARDANDO, 'Aguardando'),
    ]

    status_pagamento = models.CharField(
        max_length = 1,
        choices = TIPOS_STATUS_PAGAMENTO,
        default = STATUS_PAGAMENTO_NAO_PAGO,
    )
    status_pedido = models.CharField(
        max_length = 1,
        choices = TIPOS_STATUS_PEDIDO,
        default = STATUS_PEDIDO_AGUARDANDO,
    )

    dt_pedido = models.DateField(auto_now_add=True)
    hora_pedido = models.TimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField()