# Generated by Django 5.0.2 on 2024-02-14 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0012_area_jefe_area_historicalarea_jefe_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='historicalarea',
            name='estado',
        ),
    ]
