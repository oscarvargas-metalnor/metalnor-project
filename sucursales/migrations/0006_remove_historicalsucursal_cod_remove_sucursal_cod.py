# Generated by Django 5.0.2 on 2024-02-09 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0005_area_historicalarea_puesto_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalsucursal',
            name='cod',
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='cod',
        ),
    ]
