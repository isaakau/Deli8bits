from django.shortcuts import render
from .models import PRODUCTO

# Creamos nuestras Vistas o funciones
def home(request): #home es una funcion que siempre se llama así pero sirve para llamar a la página de inicio
    return render(request, 'postres/index.html') 
    #render = me redirigue
    #request = la llamada al index
    
def contacto(request):
    return render(request, 'postres/contacto.html')

def acercade(request):
    return render(request, 'postres/acercade.html')

def menu(request):
    return render(request, 'postres/menuProductos.html')

def form_PRODUCTO(request):
    datos = {
        'form':PRODUCTOForm()
    }

    if(request.method == 'POST'): #post guardar datos?
        formulario = PRODUCTOForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'formulario/form_vehiculo.html',datos)

def chocolateria(request):
    # listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO order by ID_PROD') 
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO WHERE CAT_PRODUCTO_ID = 1 order by ID_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/Chocolateria.html', datos)

def postres(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO WHERE CAT_PRODUCTO_ID = 2 order by ID_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/Postres.html',datos)

def tortas(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO WHERE CAT_PRODUCTO_ID = 3 order by ID_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/Tortas.html',datos)    