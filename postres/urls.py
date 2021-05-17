from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name='home'),
] #este es el primero que se ejecutas cuando sta vacío