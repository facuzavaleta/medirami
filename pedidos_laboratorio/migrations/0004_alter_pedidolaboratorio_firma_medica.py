# Generated by Django 3.2.25 on 2024-09-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_laboratorio', '0003_auto_20240824_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidolaboratorio',
            name='firma_medica',
            field=models.CharField(max_length=200),
        ),
    ]
