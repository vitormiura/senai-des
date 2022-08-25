from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=222)
    created =  models.DateTimeField(auto_now_add=True)

# Create your models here.
