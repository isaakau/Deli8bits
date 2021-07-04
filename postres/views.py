from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import PRODUCTO, USUARIO
from .forms import CustomUserForm, PRODUCTOForm, USUARIOForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required 


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
@permission_required('postres.view_producto')
def administracion(request):
    listaproductos = PRODUCTO.objects.raw('SELECT * FROM POSTRES_PRODUCTO order by ID_PROD') 
    datos = {
        'productos':listaproductos
    }
    return render(request, 'postres/administracion.html', datos)

#AGREGAR 
@permission_required('postres.add_producto')
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
@permission_required('postres.change_producto')
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
@permission_required('postres.delete_producto')
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
    return render(request, 'postres/chocolateria.html',datos)

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
@permission_required('postres.view_usuario') 
def usuarios(request):
    listausuarios = USUARIO.objects.raw('SELECT * FROM POSTRES_USUARIO order by RUT_USU') 
    datos = {
        'usuarios':listausuarios
    }
    return render(request, 'postres/usuarios.html', datos) 

#REGISTRAR USUARIO
@permission_required('postres.add_usuario')
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

#Registrar Usuario en django
def registro(request):
    datos = {
        'form':CustomUserForm()
    }
    if(request.method == 'POST'): #post guardar datos
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
        else:
            formulario = CustomUserForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'registration/registro.html',datos)

#MODIFICAR USUARIO
@permission_required('postres.change_usuario')
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
@permission_required('postres.delete_usuario')
def form_reg_del_usuario(request, id):
    usuario = USUARIO.objects.get(RUT_USU = id)
    usuario.delete()
    return redirect(to="usuarios")

#CATEGORIAS
@permission_required('postres.view_cat_producto')
def admin_categoria(request):
    return render(request, 'postres/admin_categoria.html')

#login
def loginUsu(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    return render(request, 'registration/login.html')