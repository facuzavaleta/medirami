# Generated by Django 5.0.4 on 2024-07-07 21:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_medico_user_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_asistente',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assistants', to=settings.AUTH_USER_MODEL),
        ),
    ]