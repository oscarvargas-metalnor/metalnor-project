# Generated by Django 5.0.2 on 2024-02-14 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0014_historicalsucursal_localidad_sucursal_localidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='puesto',
            name='nivel',
        ),
    ]
