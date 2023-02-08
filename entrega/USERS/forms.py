from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from USERS.models import UserProfile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True,label="Primer Nombre")
    
    class Meta:
        model=User 
        fields={"username", "first_name","email","password1","password2"}

class UpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=30,required=True,label="Username")
    first_name = forms.CharField(max_length=30,required=True,label="Primer Nombre")
    
    class Meta:
        model=User 
        fields={"username", "first_name",}

class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=["user","birth_Date", "profile_picture"]