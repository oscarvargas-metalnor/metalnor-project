# Generated by Django 5.0.2 on 2024-02-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sucursales', '0016_puesto_descripcion_puesto_nivel_jerarquico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='grupos',
            field=models.ManyToManyField(blank=True, related_name='puestos', to='auth.group'),
        ),
    ]
