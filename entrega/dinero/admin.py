from django.contrib import admin
from dinero.models import dinero

# Register your models here.
@admin.register(dinero)
class ProductAdmin(admin.ModelAdmin):
    list_display=("movimiento", "cuanto", "existe",)
    list_filter=("movimiento","cuanto")
    search_fields=("name",)
    