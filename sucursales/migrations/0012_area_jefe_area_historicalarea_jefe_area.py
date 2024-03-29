# Generated by Django 5.0.2 on 2024-02-14 12:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0011_area_estado_area_nomenclatura_historicalarea_estado_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='jefe_area',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jefe_area', to=settings.AUTH_USER_MODEL, verbose_name='Jefe de área'),
        ),
        migrations.AddField(
            model_name='historicalarea',
            name='jefe_area',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Jefe de área'),
        ),
    ]
