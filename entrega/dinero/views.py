from django.shortcuts import render
from django.http import HttpResponse
from dinero.forms import ProductForm

from dinero.models import dinero
from dinero.models import pais
from dinero.models import banco


# Create your views here.
def index(request):
    
    return render(request, "base.html",context={})

def create_product(request):
    new_movement=dinero.objects.create(movimiento="prestamo", cuanto=300, existe=True)
    print(new_movement)
    return HttpResponse ("se creo nuevo producto")

def list_products(request):
    print(request.GET)
    if 'search' in request.GET:
        busca=request.GET['search']
        all_products= dinero.objects.filter(movimiento__icontains=busca)
        all_products1= pais.objects.filter(lugar__icontains=busca)
        all_products2= banco.objects.filter(nombre__icontains=busca)

    else:
        all_products= dinero.objects.all()
        all_products1= pais.objects.all()
        all_products2= banco.objects.all()
    context={
        "products":all_products,
        "products1":all_products1,
        "products2":all_products2}
    return render(request, "list-products.html",context=context)

def formulario(request):
    if request.method=="GET":
        context={
            'form':ProductForm
        }
        return render (request,"formulario.html",context=context)
    elif request.method=="POST":
        dinero.objects.create( movimiento=request.POST["movimiento"], cuanto=request.POST["cuanto"],)
        pais.objects.create(lugar=request.POST["lugar"])
        banco.objects.create(nombre=request.POST["nombre"])
        
        return HttpResponse("Movimiento creado")