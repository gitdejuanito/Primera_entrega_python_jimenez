from django.shortcuts import render
from django.http import HttpResponse
from dinero.forms import ProductForm
from django.views.generic import DeleteView
from dinero.models import dinero
from dinero.models import pais
from dinero.models import banco
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    
    return render(request, "base.html",context={})


def create_product(request):
    new_movement=dinero.objects.create(movimiento="prestamo", cuanto=300, existe=True)
    print(new_movement)
    return HttpResponse ("se creo nuevo producto")

@login_required
def list_products(request):
    print(request.GET)
    if 'search' in request.GET:
        search=request.GET['search']
        all_products= dinero.objects.filter(movimiento__icontains=search)
        all_products= dinero.objects.filter(cuanto__icontains=search)
        all_products= dinero.objects.filter(nombre_banco__icontains=search)
        all_products= dinero.objects.filter(nombre_del_titular__icontains=search)
        all_products1= pais.objects.filter(lugar__icontains=search)
        all_products2= banco.objects.filter(nombre__icontains=search)

    else:
        all_products= dinero.objects.all()
        all_products1= pais.objects.all()
        all_products2= banco.objects.all()
    context={
        "products":all_products,
        "products1":all_products1,
        "products2":all_products2}
    return render(request, "list-products.html",context=context)

@login_required
def formulario(request):
    if request.method=="GET":
        context={
            'form':ProductForm
        }
        return render (request,"formulario.html",context=context)
    elif request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            dinero.objects.create( 
                movimiento=form.cleaned_data["movimiento"], 
                cuanto=form.cleaned_data["cuanto"],
                nombre_banco=form.cleaned_data["nombre_banco"],
                nombre_del_titular=form.cleaned_data["nombre_del_titular"],
                )
            
            return render (request,"formulario.html",context={}) and HttpResponse("Movimiento creado")
        else:
            context={"form_errors": form.errors,
            "form":ProductForm
            }
        return render (request,"formulario.html",context={}) and HttpResponse("Movimiento rechazado, porfavor vuelva a intentarlo")
        
class delete(DeleteView):
    model=dinero
    fields="__all__"
    template_name="moveDelete.html"
    success_url="/list-product/"