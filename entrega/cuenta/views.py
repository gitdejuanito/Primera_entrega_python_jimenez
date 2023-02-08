from django.shortcuts import render
from cuenta.models import Cuenta
from cuenta.forms import CuentaForm
from django.http import HttpResponse
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def cuentas_list(request):
    cuentas=Cuenta.objects.filter(is_active=True)
    context={
        "cuentas":cuentas
    }
    return render(request, "cuenta-list.html",context=context)

@login_required
def cuentas_create(request):
    if request.method=="GET":
        context={
            'form':CuentaForm
        }
        return render (request,"formularioCuenta.html",context=context)
    elif request.method=="POST":
        form=CuentaForm(request.POST)
        if form.is_valid():
            Cuenta.objects.create( 
                Nombre_del_titular=form.cleaned_data["Nombre_del_titular"], 
                Banco=form.cleaned_data["Banco"],
                Numero_de_cuenta=form.cleaned_data["Numero_de_cuenta"],
                Codigo_Postal=form.cleaned_data["Codigo_Postal"],
                )
            
            return render(request,"formularioCuenta.html",context={}) and HttpResponse("Cuenta creada")
            
        else:
            context={"form_errors": form.errors,
            "form":CuentaForm
            }
        return render (request,"formularioCuenta.html",context={}) and HttpResponse("Cuenta rechazado, porfavor vuelva a intentarlo")

def cuentas_update(request, id):
    Count =Cuenta.objects.get(id=id)
    if request.method=="GET":
        context={
            'form':CuentaForm(
                initial={
                    "Nombre_del_titular":Count.Nombre_del_titular,
                    "Banco":Count.Banco,
                    "Numero_de_cuenta":Count.Numero_de_cuenta,
                    "Codigo_Postal":Count.Codigo_Postal,
                }
            )
        } 
        return render (request,"cuentaUpdate.html",context=context)
    elif request.method=="POST":
        form=CuentaForm(request.POST)
        if form.is_valid():
            Cuenta.objects.filter(id=id).update( 
                Nombre_del_titular=form.cleaned_data["Nombre_del_titular"], 
                Banco=form.cleaned_data["Banco"],
                Numero_de_cuenta=form.cleaned_data["Numero_de_cuenta"],
                Codigo_Postal=form.cleaned_data["Codigo_Postal"],
                )
            
            return render(request,"cuentaUpdate.html",context={}) and HttpResponse("Cuenta actualizada ")
        else:
            context={"form_errors": form.errors,
            "form":CuentaForm
            }
            return render (request,"cuentasUpdate.html",context=context) and HttpResponse("Cuenta rechazada, porfavor vuelva a intentarlo")

class CuentaDeleteView(DeleteView):
    model=Cuenta
    fields= "_all_"
    template_name="cuentaDelete.html"
    success_url="/cuenta/cuenta-list/"

