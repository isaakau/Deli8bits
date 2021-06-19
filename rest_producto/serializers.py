from rest_framework import serializers
from postres.models import PRODUCTO

class PRODUCTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUCTO
        fields = ['ID_PROD', 'NOM_PROD', 'DESC_PROD', 'PRECIO_PROD','UNIDAD_PROD','CAT_PRODUCTO', 'IMAGEN_PROD']
