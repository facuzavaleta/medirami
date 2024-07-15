from django.db import models
from pacientes.models import Paciente
from users.models import CustomUser
from django.utils import timezone
from datetime import timedelta

class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='recetas')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recetas')
    fecha = models.DateField(auto_now_add=True)
    medicacion = models.CharField(max_length=200)
    droga = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    marca_recomendada = models.CharField(max_length=100, blank=True, null=True)
    cantidad_unidades = models.IntegerField()
    firma_medica = models.CharField(max_length=200)
    qr_codigo_barras = models.CharField(max_length=100, unique=True)
    fecha_ultimo_laboratorio = models.DateField()
    proxima_fecha_empadronamiento = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    viewed = models.BooleanField(default=False)
    tiempo_de_vida = models.DurationField(default=timedelta(days=7))  # Default tiempo de vida de 7 días

    def __str__(self):
        return f"Receta de {self.paciente} por {self.user} - {self.medicacion}"

    def is_expired(self):
        expiration_date = self.fecha + self.tiempo_de_vida
        return timezone.now() > expiration_date
