from django.db import models

# Create your models here.

class pais(models.Model):
    lugar=models.CharField(max_length=100)

class banco(models.Model):
    nombre=models.CharField(max_length=100)


class dinero(models.Model):
    movimiento= models.CharField(max_length=100)
    cuanto=models.FloatField()
    existe=models.BooleanField(default=True)

