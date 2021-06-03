from django.urls import path
from .views import home, contacto, acercade, menu, chocolateria, postres,tortas,form_PRODUCTO,form_mod_PRODUCTO,form_del_PRODUCTO

urlpatterns = [
    path('',home,name='home'),
    path('contacto',contacto,name='contacto'),
    path('acercade',acercade,name='acercade'),
    path('menu',menu,name='menu'),
    path('chocolateria',chocolateria,name='chocolateria'),
    path('postres',postres,name='postres'),
    path('tortas',tortas,name='tortas'),
    path('agregar-producto',form_PRODUCTO,name='form_producto'),
    path('modificar-producto/<id>',form_mod_PRODUCTO,name='form_mod_producto'),
    path('eliminar-producto/<id>',form_del_PRODUCTO,name='form_del_producto'),
] #este es el primero que se ejecutas cuando sta vacío