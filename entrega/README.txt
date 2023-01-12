							CONSULTA DE MOVIMIENTOS BANCARIOS

Backend

1. Se crean los modelos y las clases de los datos que queremos consultar en el front.
2. Despues creamos de esas mismas clases y modelos un archivo "forms.py" para llamar un formulario desde el front.
3. En el archivo views.py se declaran la funcion formulario para especificar las acciones cuando se obtenga un request tipo 
GET and POST.
	3.1 De igual manera se crean los filtros de los objetos creados para poder buscarlos en el front.

4. Seguido de esto en urls.py, se crean los urls para cada funcion declarada en views.
5. Despues se creó un base.html que es el padre en diseño de todos los htmls de este proyecto
6. Se modifican ciertas caracteristicas individualmente que deben tener los htmls para mostrarse en el front.


FRONT

1.Entrar a la http://127.0.0.1:8000/formulario/ para crear la consulta de movimientos
2.Ir a http://127.0.0.1:8000/list-product/ para checar todos los movimientos consultados.




