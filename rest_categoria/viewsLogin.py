from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

#Login por django sin Oracle? tira el token que se guarda en la BD ?
@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request) #creo que esto hace que sea en JSON                  
    print('************************************')
    username = data['username'] #lo que esta entre comillas tiene que ser lo mismo que en el HTML
    password = data['password']
    print(data)
    
    #se valida usuario 
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    #se valida la contraseña
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password incorrecta")
    
    #crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    return Response(token.key)


