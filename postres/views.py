from django.shortcuts import redirect, render
from .models import PRODUCTO, USUARIO
from .forms import PRODUCTOForm, USUARIOForm

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

#MANTENEDOR DE PRODUCTOS (Listar)
def administracion(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO order by ID_PROD') 
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
        else:
            formulario = PRODUCTOForm()
            datos['mensaje'] = 'ERROR: No se ha guardado el producto, intente nuevamente'
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
            return redirect(to="administracion")
        else:
            formulario = PRODUCTOForm()
            datos['mensaje'] = 'ERROR: No se ha modificado el producto, intente nuevamente'
    return render(request,'postres/form_mod_prod.html',datos)    

#ELIMINAR PRODUCTO
def form_del_prod(request, id):
    producto = PRODUCTO.objects.get(ID_PROD = id)
    producto.delete()
    return redirect(to="administracion")

#LISTAR SOLO CHOCOLATES
def chocolateria(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO WHERE CAT_PRODUCTO_ID = 1 order by NOM_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/Chocolateria.html', datos)

#LISTAR SOLO LOS POSTRES
def postres(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO WHERE CAT_PRODUCTO_ID = 2 order by NOM_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/Postres.html',datos)

#LISTAR SOLO TORTAS
def tortas(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO WHERE CAT_PRODUCTO_ID = 3 order by NOM_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/Tortas.html',datos)   

#LISTA DE USUARIOS 
def usuarios(request):
    listausuarios = USUARIO.objects.raw('SELECT * FROM POSTRES_USUARIO order by RUT_USU') 
    datos = {
        'usuarios':listausuarios
    }
    return render(request, 'postres/usuarios.html', datos) 

#REGISTRAR USUARIO
def form_reg_usuario(request):
    datos = {
        'form':USUARIOForm()
    }
    if(request.method == 'POST'): #post guardar datos
        formulario = USUARIOForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
        else:
            formulario = USUARIOForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'postres/form_reg_usuario.html',datos)

def registro(request):
    datos = {
        'form':USUARIOForm()
    }
    if(request.method == 'POST'): #post guardar datos
        formulario = USUARIOForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
        else:
            formulario = USUARIOForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'postres/registro.html',datos)

#MODIFICAR USUARIO
def form_reg_mod_usuario(request,id):
    usuario = USUARIO.objects.get(RUT_USU = id)
    datos = {
        'form':USUARIOForm(instance=usuario)
    }
    
    if(request.method == 'POST'): #post guardar datos?
        formulario = USUARIOForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario Modificado correctamente'
            return redirect(to= "usuarios")
        else:
            formulario = USUARIOForm()
            datos['mensaje'] = 'ERROR: No se ha modificado, intente nuevamente'
    return render(request,'postres/form_reg_mod_usuario.html',datos)      

#ELIMINAR USUARIO
def form_reg_del_usuario(request, id):
    usuario = USUARIO.objects.get(RUT_USU = id)
    usuario.delete()
    return redirect(to="usuarios")