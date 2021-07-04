from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import PRODUCTO, USUARIO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PRODUCTOForm(ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ['ID_PROD', 'NOM_PROD', 'DESC_PROD', 'PRECIO_PROD','UNIDAD_PROD','CAT_PRODUCTO', 'IMAGEN_PROD']

class USUARIOForm(ModelForm):
    class Meta:
        model = USUARIO
        fields = ['RUT_USU', 'PASS_USU', 'NOM_USU', 'APE_USU','MAIL_USU','NUMTEL_USU', 'DIREC_USU']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
