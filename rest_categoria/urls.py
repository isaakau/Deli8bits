from django.urls import path
from rest_categoria.views import categoria_producto

urlpatterns = [
    path('categoria_producto', categoria_producto, name="categoria_producto"),
]