from unicodedata import category
from django.db import models

class Categoria(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category
class Produto(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title