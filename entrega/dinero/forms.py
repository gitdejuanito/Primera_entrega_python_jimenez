from django import forms

class ProductForm (forms.Form):
    movimiento= forms.CharField(max_length=100)
    lugar=forms.CharField(max_length=100)
    cuanto =forms.FloatField()
    existe=forms.BooleanField(required=False)
    nombre=forms.CharField(max_length=100)

    


