from django.db import models

# Create your models here.
class Cuenta(models.Model):
    CONDITION_CHOICES= (
        ("CITI","CITI"),
        ("SANTANDER","SANTANDER"),
        ("BBVA","BBVA"),
    )



    Nombre_del_titular=models.CharField(max_length=35)
    Banco=models.CharField(max_length=30, choices=CONDITION_CHOICES)
    Numero_de_cuenta=models.BigIntegerField()
    Codigo_Postal=models.BigIntegerField()
    is_active=models.BooleanField(default=True)