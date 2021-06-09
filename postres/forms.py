from django import forms
from django.forms import ModelForm
from .models import PRODUCTO

class PRODUCTOForm(ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ['ID_PROD', 'IMAGEN_PROD', 'NOM_PROD', 'DESC_PROD', 'PRECIO_PROD','CAT_PRODUCTO']