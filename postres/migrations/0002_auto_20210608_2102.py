# Generated by Django 3.2.2 on 2021-06-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='IMAGEN_PROD',
            field=models.ImageField(null=True, upload_to='img_productos', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='DESC_PROD',
            field=models.CharField(blank=True, max_length=100, verbose_name='Descripción'),
        ),
    ]
