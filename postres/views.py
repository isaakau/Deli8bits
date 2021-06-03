from django.shortcuts import render,redirect
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
    listaproductos = PRODUCTO.objects.all() #hace un Select * a la tabla
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/menuProductos.html',datos)

def form_PRODUCTO(request):
    datos = {
        'form':PRODUCTOForm()
    }
    if(request.method == 'POST'): #post guardar datos?
        formulario = PRODUCTOForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'postres/form_producto.html',datos)

def form_mod_PRODUCTO(request,id):
    producto = PRODUCTO.objects.get(ID_PROD = id)
    datos = {
        'form':PRODUCTOForm(instance=producto)
    }
    if(request.method == 'POST'): #post guardar datos?
        formulario = PRODUCTOForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'
    return render(request,'postres/form_mod_producto.html',datos)    

def form_del_PRODUCTO(id):
    producto = PRODUCTO.objects.get(ID_PROD = id)
    producto.delete()
    return redirect(to="menu")
def chocolateria(request):
    return render(request, 'postres/Chocolateria.html')

def postres(request):
    return render(request, 'postres/Postres.html')

def tortas(request):
    return render(request, 'postres/Tortas.html')    