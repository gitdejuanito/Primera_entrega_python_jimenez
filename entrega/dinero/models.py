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
    nombre_banco=models.CharField(max_length=100,default=True)
    nombre_del_titular=models.CharField(max_length=100,default=True)

    def __str__(self):
        return self.movimiento
    
    class Meta:
        verbose_name="Dinero"
        verbose_name_plural="Movimientos con dinero"
