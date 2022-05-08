from django.db import models
import datetime
# Create your models here.

class familiares(models.Model):

    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Edad = models.IntegerField()
    Parentesco = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.Nombre} {self.Apellido} {self.Edad} {self.Parentesco}'