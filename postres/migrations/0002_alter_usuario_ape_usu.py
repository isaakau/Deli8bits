# Generated by Django 3.2.2 on 2021-05-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='APE_USU',
            field=models.CharField(max_length=60, verbose_name='Apellidos'),
        ),
    ]