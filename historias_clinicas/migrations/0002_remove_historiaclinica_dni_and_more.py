# Generated by Django 5.0.4 on 2024-07-01 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historias_clinicas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiaclinica',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='numero_afiliado',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='obra_social',
        ),
        migrations.RemoveField(
            model_name='historiaclinica',
            name='sexo',
        ),
    ]
