from django.urls import path
from rest_categoria.views import categoria_producto,detalle_categoria

urlpatterns = [
    path('categoria-producto', categoria_producto, name="categoria_producto"),
    path('detalle-categoria/<id>',detalle_categoria,name='detalle_categoria'),
]