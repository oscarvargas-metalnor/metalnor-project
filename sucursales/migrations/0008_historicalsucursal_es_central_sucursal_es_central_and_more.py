# Generated by Django 5.0.2 on 2024-02-09 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0007_area_cambiado_por_historicalarea_cambiado_por_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsucursal',
            name='es_central',
            field=models.BooleanField(default=False, help_text='Indica si la sucursal es la central del negocio.', verbose_name='¿Es central?'),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='es_central',
            field=models.BooleanField(default=False, help_text='Indica si la sucursal es la central del negocio.', verbose_name='¿Es central?'),
        ),
        migrations.AlterField(
            model_name='historicalsucursal',
            name='alias',
            field=models.CharField(help_text='El alias de la sucursal.', max_length=350, verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='historicalsucursal',
            name='codigo',
            field=models.CharField(help_text='El código de la sucursal.', max_length=350, verbose_name='codigo'),
        ),
        migrations.AlterField(
            model_name='historicalsucursal',
            name='responsable',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='El responsable de la sucursal.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Responsable'),
        ),
        migrations.AlterField(
            model_name='historicalsucursal',
            name='tipo',
            field=models.CharField(choices=[('Micro', 'Micro'), ('Chica', 'Chica'), ('Mediana', 'Mediana'), ('Grande', 'Grande')], help_text='El tipo de sucursal (tamaño).', max_length=350, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='alias',
            field=models.CharField(help_text='El alias de la sucursal.', max_length=350, verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='codigo',
            field=models.CharField(help_text='El código de la sucursal.', max_length=350, verbose_name='codigo'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='responsable',
            field=models.ForeignKey(help_text='El responsable de la sucursal.', on_delete=django.db.models.deletion.PROTECT, related_name='sucursales', to=settings.AUTH_USER_MODEL, verbose_name='Responsable'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='tipo',
            field=models.CharField(choices=[('Micro', 'Micro'), ('Chica', 'Chica'), ('Mediana', 'Mediana'), ('Grande', 'Grande')], help_text='El tipo de sucursal (tamaño).', max_length=350, verbose_name='Tipo'),
        ),
    ]
