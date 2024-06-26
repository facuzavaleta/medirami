# Generated by Django 5.0.4 on 2024-07-01 02:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='historia_clinica',
        ),
        migrations.AddField(
            model_name='paciente',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pacientes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='provincia',
            field=models.CharField(choices=[('Buenos Aires', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'), ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'), ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'), ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'), ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'), ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'), ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'), ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán')], max_length=100),
        ),
    ]
