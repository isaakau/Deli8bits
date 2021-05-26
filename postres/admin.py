from django.contrib import admin
from .models import CAT_PRODUCTO, PRODUCTO, USUARIO

# Register your models here.

admin.site.register(CAT_PRODUCTO)
admin.site.register(PRODUCTO)
admin.site.register(USUARIO)