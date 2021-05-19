from django.urls import path
from .views import home, contacto, acercade, menu

urlpatterns = [
    path('',home,name='home'),
    path('/contacto',contacto,name='contacto'),
    path('/acercade',acercade,name='acercade'),
    path('/menu',menu,name='menu'),
] #este es el primero que se ejecutas cuando sta vacío