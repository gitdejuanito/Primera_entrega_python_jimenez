from django.contrib import admin
from cuenta.models import Cuenta
# Register your models here.
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display=("Numero_de_cuenta","Banco","Nombre_del_titular",)
    list_filter=("Banco",)
    search_fields=("Nombre_del_titular",)
