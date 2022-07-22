from django.db import models

class Agenda(models.Model):
    name = models.CharField(max_length=66)
    description = models.CharField(max_length=255)
    #is_active = models.BooleanField()
    teste = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return self.name