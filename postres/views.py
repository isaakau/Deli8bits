from django.shortcuts import redirect, render
from .models import PRODUCTO
from .forms import PRODUCTOForm

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

def administracion(request):
    listaproductos = PRODUCTO.objects.all() #hace un Select * a la tabla
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/administracion.html', datos)

#AGREGAR PRODUCTO
def form_prod(request):
    datos = {
        'form':PRODUCTOForm()
    }
    if(request.method == 'POST'): #post guardar datos?
        formulario = PRODUCTOForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'
    return render(request,'postres/form_prod.html',datos)

#MODIFICAR PRODUCTO
def form_mod_prod(request,id):
    producto = PRODUCTO.objects.get(ID_PROD = id)
    datos = {
        'form':PRODUCTOForm(instance=producto)
    }
    
    if(request.method == 'POST'): #post guardar datos?
        formulario = PRODUCTOForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'
    return render(request,'postres/form_mod_prod.html',datos)    

#ELIMINAR PRODUCTO
def form_del_prod(request, id):
    producto = PRODUCTO.objects.get(ID_PROD = id)
    producto.delete()
    return redirect(to="administracion")

def chocolateria(request):
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