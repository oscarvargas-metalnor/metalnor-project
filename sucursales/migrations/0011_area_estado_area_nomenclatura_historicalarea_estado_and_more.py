# Generated by Django 5.0.2 on 2024-02-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0010_tiposucursal_remove_historicalsucursal_es_central_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='estado',
            field=models.CharField(choices=[('Activo', 'A'), ('Baja', 'B')], default='Activo', max_length=100, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='area',
            name='nomenclatura',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nomenclatura'),
        ),
        migrations.AddField(
            model_name='historicalarea',
            name='estado',
            field=models.CharField(choices=[('Activo', 'A'), ('Baja', 'B')], default='Activo', max_length=100, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='historicalarea',
            name='nomenclatura',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nomenclatura'),
        ),
    ]
