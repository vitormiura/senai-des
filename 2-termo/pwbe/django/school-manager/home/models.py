from distutils.command.upload import upload
from django.db import models
from stdimage import StdImageField

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField()
    email = models.EmailField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = StdImageField(upload_to='foto')

    def __str__(self):
        return self.nome