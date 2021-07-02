from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from postres.models import CAT_PRODUCTO
from rest_categoria.serializers import CAT_PRODUCTOSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
#CATEGORIAS DE PRODUCTOS EN JSON 
def categoria_producto(request):
    if request.method == 'GET':
        categoria = CAT_PRODUCTO.objects.all().order_by('ID_CATPROD')
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

#DETALLES DE LAS CATEGORIAS EN JSON (OBTENER, MODIFICAR Y BORRAR)
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
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
        if(categoria.delete()):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NOT_CONTENT)            