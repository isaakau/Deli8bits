from django.urls import path
from .views import home, contacto, acercade, menu, chocolateria, postres,tortas

urlpatterns = [
    path('',home,name='home'),
    path('/contacto',contacto,name='contacto'),
    path('/acercade',acercade,name='acercade'),
    path('/menu',menu,name='menu'),
    path('/chocolateria',chocolateria,name='chocolateria'),
    path('/postres',postres,name='postres'),
    path('/tortas',tortas,name='tortas'),
] #este es el primero que se ejecutas cuando sta vacío