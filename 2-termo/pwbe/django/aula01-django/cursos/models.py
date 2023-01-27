from django.db import models

class Cursos(models.Model):
    nome_curso_bosch = models.CharField(max_length=50)
    nome_curso_senai = models.CharField(max_length=50)
    duracao_bosch = models.IntegerField()
    duracao_senai = models.IntegerField()
    qtd_aprendizes = models.IntegerField()
    desc = models.TextField()
    more_info = models.CharField(max_length=100)