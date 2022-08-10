from django.db import models

class Aluno(models.model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome