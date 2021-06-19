from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from postres.models import CAT_PRODUCTO
from rest_categoria.serializers import CAT_PRODUCTOSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])

#CATEGORIAS DE PRODUCTOS EN JSON 
def categoria_producto(request):
    if request.method == 'GET':
        producto = CAT_PRODUCTO.objects.all()
        serializer = CAT_PRODUCTOSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CAT_PRODUCTOSerializer(data=data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)