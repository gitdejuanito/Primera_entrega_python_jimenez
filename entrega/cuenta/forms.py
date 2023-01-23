from django import forms
class CuentaForm(forms.Form):
    Nombre_del_titular=forms.CharField(max_length=35)
    Banco=forms.CharField(max_length=30)
    Numero_de_cuenta=forms.IntegerField()
    Codigo_Postal=forms.IntegerField()
    