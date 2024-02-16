# Generated by Django 5.0.2 on 2024-02-15 14:07

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0023_area_correo_electronico_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalJerarquia',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cambiado_por', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cambiado por')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical jerarquia',
                'verbose_name_plural': 'historical jerarquias',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Jerarquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('cambiado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_history', to=settings.AUTH_USER_MODEL, verbose_name='Cambiado por')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='area',
            name='jerarquia',
            field=models.ForeignKey(blank=True, help_text='La jerarquía de la área', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='areas', to='sucursales.jerarquia', verbose_name='Jerarquía'),
        ),
        migrations.AddField(
            model_name='historicalarea',
            name='jerarquia',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='La jerarquía de la área', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sucursales.jerarquia', verbose_name='Jerarquía'),
        ),
    ]
