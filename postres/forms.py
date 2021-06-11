from django import forms
from django.forms import ModelForm
from .models import PRODUCTO, USUARIO

class PRODUCTOForm(ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ['ID_PROD', 'NOM_PROD', 'DESC_PROD', 'PRECIO_PROD','UNIDAD_PROD','CAT_PRODUCTO', 'IMAGEN_PROD']

class USUARIOForm(ModelForm):
    class Meta:
        model = USUARIO
        fields = ['RUT_USU', 'PASS_USU', 'NOM_USU', 'APE_USU','MAIL_USU','NUMTEL_USU', 'DIREC_USU']