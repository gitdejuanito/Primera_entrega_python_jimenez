from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,  authenticate


# Create your views here.
def login_view(request):
    if request.method=="GET":
        form=AuthenticationForm()
        context={
            "form":form
        }
        return render (request, "login.html", context=context)
    
    elif request.method=="POST":
        form=AuthenticationForm(request=request, data =request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            user=authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                context={
                    "message":f"Bienvenido {username}"
                }
                return render(request,"base.html",context=context)
            
            
        form=AuthenticationForm()
        context={
                    "form":form,
                    "errors":"Usename o password incorrectos"

                    } 
        return render(request,"login.html", context=context)

def register_view(request):
    if request.method=="GET":
        form=UserCreationForm()
        context={ "form":form
        }

        return render(request,"register.html",context=context)
    
    elif request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')