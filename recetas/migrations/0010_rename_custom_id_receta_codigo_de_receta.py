# Generated by Django 3.2.25 on 2024-09-03 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0009_receta_custom_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='custom_id',
            new_name='codigo_de_receta',
        ),
    ]
