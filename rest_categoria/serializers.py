from rest_framework import serializers
from postres.models import CAT_PRODUCTO

class CAT_PRODUCTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAT_PRODUCTO
        fields = ['ID_CATPROD', 'NOM_CATPROD']