"""entrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from dinero.views import create_product, list_products, index, formulario
from entrega.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from dinero.views import delete
urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path ('create-product/',create_product),
    path ('list-product/' , list_products),
    path ('formulario/' , formulario),
    
    path ("cuenta/", include("cuenta.urls")),
    path ("USERS/", include("USERS.urls")),
    path ('moveDelete/<int:pk>/' , delete.as_view()),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
