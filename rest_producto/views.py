from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from postres.models import PRODUCTO
from rest_producto.serializers import PRODUCTOSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])

#LISTA TODOS LOS PRODUCTOS EN JSON 
def lista_productos(request):
    if request.method == 'GET':
        producto = PRODUCTO.objects.all()
        serializer = PRODUCTOSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PRODUCTOSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DETALLES DE LOS PRODUCTOS EN JSON (OBTENER, MODIFICAR Y BORRAR)
@api_view(['GET','PUT','DELETE'])
def detalle_categoria(request,id):
    try:
        producto = PRODUCTO.objects.get(ID_PROD=id)
    except PRODUCTO.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PRODUCTOSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PRODUCTOSerializer(producto,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)       