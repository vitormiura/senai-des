from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

class Curso(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    ativo = models.CharField(max_length=5, choices=(('A','Ativo'),('I','Inativo'),))