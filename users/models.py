from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_medico = models.BooleanField(default=False)
    is_asistente = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Cambia el related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Cambia el related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Medico(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()

class AsistenteMedico(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, related_name="asistentes", on_delete=models.CASCADE)
    email = models.EmailField()