from django.contrib import admin

from django.urls import path
from cuenta.views import cuentas_list
from cuenta.views import cuentas_create
from cuenta.views import cuentas_update, CuentaDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path("cuenta-list/", cuentas_list ),
    path("cuenta-create/", cuentas_create ),
    path ("cuentas-update/<int:id>/",cuentas_update ),
    path("cuenta-delete/<int:pk>/", CuentaDeleteView.as_view()  ),
    
]