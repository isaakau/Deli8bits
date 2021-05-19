from django.urls import path
from .views import home, contacto

urlpatterns = [
    path('',home,name='home'),
    path('',contacto,name='contacto'),
] #este es el primero que se ejecutas cuando sta vacío