from django.urls import path
from .views import home, contacto, acercade, menu, chocolateria, postres, tortas, administracion, usuarios, form_prod, form_mod_prod, form_del_prod,form_reg_usuario,form_reg_mod_usuario, form_reg_del_usuario,registro,admin_categoria, loginUsu
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home'),
    path('contacto',contacto,name='contacto'),
    path('acercade',acercade,name='acercade'),
    path('menu',menu,name='menu'),
    path('chocolateria',chocolateria,name='chocolateria'),
    path('postres',postres,name='postres'),
    path('tortas',tortas,name='tortas'),
    path('administracion',administracion,name='administracion'),
    path('usuario',usuarios,name='usuarios'), 
    path('agregar-producto',form_prod, name='form_prod'),
    path('modificar-producto/<id>',form_mod_prod,name='form_mod_prod'),
    path('eliminar-producto/<id>',form_del_prod,name='form_del_prod'),
    path('agregar-usuario',form_reg_usuario,name='form_reg_usuario'),
    path('modificar-usuario/<id>',form_reg_mod_usuario,name='form_reg_mod_usuario'),
    path('eliminar-usuario/<id>',form_reg_del_usuario,name='form_reg_del_usuario'),
    path('registro-usuario',registro,name='registro'),
    path('admin-categoria',admin_categoria,name='admin_categoria'),
    path('login',loginUsu,name='loginUsu'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
