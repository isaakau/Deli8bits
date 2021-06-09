from django.urls import path
from .views import home, contacto, acercade, menu, chocolateria, postres, tortas, administracion, form_prod, form_mod_prod, form_del_prod

urlpatterns = [
    path('',home,name='home'),
    path('contacto',contacto,name='contacto'),
    path('acercade',acercade,name='acercade'),
    path('menu',menu,name='menu'),
    path('chocolateria',chocolateria,name='chocolateria'),
    path('postres',postres,name='postres'),
    path('tortas',tortas,name='tortas'),
    path('administracion',administracion,name='administracion'),
    path('form_prod',form_prod, name='form_prod'),
    path('modificar-producto/<id>',form_mod_prod,name='form_mod_prod'),
    path('eliminar-producto/<id>',form_del_prod,name='form_del_prod'),
] #este es el primero que se ejecutas cuando sta vacío