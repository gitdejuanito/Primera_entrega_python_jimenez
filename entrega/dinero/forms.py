from django import forms

class ProductForm (forms.Form):
    movimiento= forms.CharField(max_length=100)
    cuanto =forms.FloatField()
    existe=forms.BooleanField(required=False)
    nombre_del_titular=forms.CharField(max_length=100)
    nombre_banco=forms.CharField(max_length=100)


#html 

#<form action="" method="POST">
    #{% csrf_token %}
    #<p> Nombre: <input type="text" name="name"> </p>
    #<p> Precio: <input type="number" name="price"> </p>
    


