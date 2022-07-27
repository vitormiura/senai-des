from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    active = models.BooleanField()