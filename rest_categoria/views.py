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
        categoria = CAT_PRODUCTO.objects.all()
        serializer = CAT_PRODUCTOSerializer(categoria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CAT_PRODUCTOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DETALLES DE LAS CATEGORIAS EN JSON 
@api_view(['GET','PUT','DELETE'])
def detalle_categoria(request,id):
    try:
        categoria = CAT_PRODUCTO.objects.get(ID_CATPROD=id)
    except CAT_PRODUCTO.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CAT_PRODUCTOSerializer(categoria)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CAT_PRODUCTOSerializer(categoria,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)            