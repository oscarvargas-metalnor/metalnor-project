# Generated by Django 5.0.2 on 2024-02-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_ordernote_order_date_ordernote_production_manager_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderNote',
        ),
    ]
