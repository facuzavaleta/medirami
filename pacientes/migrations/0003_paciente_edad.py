# Generated by Django 3.2.25 on 2024-07-12 14:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_remove_paciente_historia_clinica_paciente_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
