from django.contrib import admin

from django.urls import path
from dinero.views import create_product, list_products, index, formulario

urlpatterns = [
    path (' ',index, name='index'),
    path('admin/', admin.site.urls),
    path ('create-product/',create_product),
    path ('list-product/' , list_products),
    path ('formulario/' , formulario),
]