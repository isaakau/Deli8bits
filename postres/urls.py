from django.urls import path
from .views import home, contacto, acercade, menu, chocolateria, postres, tortas, administracion, form_prod, form_mod_prod, form_del_prod
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
    path('agregar-producto',form_prod, name='form_prod'),
    path('modificar-producto/<id>',form_mod_prod,name='form_mod_prod'),
    path('eliminar-producto/<id>',form_del_prod,name='form_del_prod'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)