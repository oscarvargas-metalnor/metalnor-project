# Generated by Django 5.0.2 on 2024-02-09 17:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0006_remove_historicalsucursal_cod_remove_sucursal_cod'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='cambiado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_history', to=settings.AUTH_USER_MODEL, verbose_name='Cambiado por'),
        ),
        migrations.AddField(
            model_name='historicalarea',
            name='cambiado_por',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cambiado por'),
        ),
        migrations.AddField(
            model_name='historicalsucursal',
            name='cambiado_por',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cambiado por'),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='cambiado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_history', to=settings.AUTH_USER_MODEL, verbose_name='Cambiado por'),
        ),
    ]
