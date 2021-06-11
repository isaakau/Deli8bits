from django.db import models

# Create your models here.

#modelo para CATEGORIA DEL PRODUCTO 
class CAT_PRODUCTO(models.Model):
    ID_CATPROD = models.IntegerField(primary_key=True,max_length=2,verbose_name='ID de la categoria')
    NOM_CATPROD = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.NOM_CATPROD

#Modelopara el PRODUCTO 
class PRODUCTO(models.Model):
    ID_PROD = models.CharField(max_length=4,primary_key=True, verbose_name='Id')
    NOM_PROD = models.CharField(max_length=30, verbose_name='Nombre')
    DESC_PROD = models.CharField(max_length=200, blank=True, verbose_name='Descripción')
    PRECIO_PROD = models.IntegerField(null=True,verbose_name='Precio')
    UNIDAD_PROD = models.CharField(max_length=30, verbose_name='Unidad')
    CAT_PRODUCTO = models.ForeignKey(CAT_PRODUCTO, on_delete=models.CASCADE, verbose_name='Categoria')
    IMAGEN_PROD = models.ImageField (null=True,verbose_name='Imagen')#campo de imagen
    
    def __str__(self):
        return self.NOM_PROD

#crear tabla usuario para registrar usuarios, por mientras 
class USUARIO(models.Model):
    RUT_USU = models.CharField(max_length=9,primary_key=True, verbose_name='Rut (sin punto ni guión)')
    PASS_USU = models.CharField(max_length=20,verbose_name='Contraseña')
    NOM_USU = models.CharField(max_length=30,verbose_name='Nombre')
    APE_USU = models.CharField(max_length=60,verbose_name='Apellidos')
    MAIL_USU = models.CharField(max_length=100,verbose_name='Mail')
    NUMTEL_USU = models.IntegerField(verbose_name='Teléfono')
    DIREC_USU = models.CharField(max_length=300,verbose_name='Dirección')

    def __str__(self):
        return self.RUT_USU