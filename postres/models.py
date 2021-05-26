from django.db import models

# Create your models here.

#modelo para CATEGORIA DEL PRODUCTO 
class CAT_PRODUCTO(models.Model):
    ID_CATPROD = models.IntegerField(primary_key=True,max_length=2,verbose_name='ID de categoria producto')
    NOM_CATPROD = models.CharField(max_length=50,verbose_name='Nombre de la categoria producto')

    def __str__(self):
        return self.NOM_CATPROD

#Modelopara el PRODUCTO 
class PRODUCTO(models.Model):
    ID_PROD = models.CharField(max_length=4,primary_key=True, verbose_name='Id del Producto')
    NOM_PROD = models.CharField(max_length=30, verbose_name='Nombre del producto')
    DESC_PROD = models.CharField(max_length=100,null=True, blank=True, verbose_name='Descripción del produto')
    PRECIO_PROD = models.IntegerField(max_length=6,null=True,verbose_name='Precio del producto')
    CAT_PRODUCTO = models.ForeignKey(CAT_PRODUCTO, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NOM_PROD