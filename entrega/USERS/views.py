from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,  authenticate
from django.contrib.auth.models import User
from USERS.forms import RegisterForm
from USERS.forms import UpdateForm

from django.contrib.auth.decorators import login_required
from USERS.forms import UserProfile


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
                    "message":f"Hola {username}"
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
        form=RegisterForm()
        context={ "form":form
        }
 
        return render(request,"register.html",context=context)
    
    elif request.method =="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
    context={
        "errors":form.errors,
        "form":RegisterForm
    }
    return render(request,"register.html",context=context)

@login_required
def update_view(request):
    user=request.user
    if request.method =="GET":
        form=UpdateForm(initial={
            "username":user.username,
            "first_name":user.first_name,
            
        })
        context ={
            "form":form
        }
        return render(request, "update.html", context=context)
    
    elif request.method=="POST":
        form=UpdateForm(request.POST)
        if form.is_valid():
            user.username=form.cleaned_data.get("username")
            user.first_name=form.cleaned_data.get("first_name")
            user.save()
            return redirect("login")


def about_me(request):
    if request.method =="GET":
        return render(request, "about.html", context={})
