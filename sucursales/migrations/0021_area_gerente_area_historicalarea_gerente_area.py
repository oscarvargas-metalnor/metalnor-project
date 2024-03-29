# Generated by Django 5.0.2 on 2024-02-15 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0020_remove_puesto_grupos_remove_puesto_permisos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='gerente_area',
            field=models.OneToOneField(blank=True, help_text='El gerente de la área', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gerente_area', to=settings.AUTH_USER_MODEL, verbose_name='Gerente de área'),
        ),
        migrations.AddField(
            model_name='historicalarea',
            name='gerente_area',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='El gerente de la área', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Gerente de área'),
        ),
    ]
