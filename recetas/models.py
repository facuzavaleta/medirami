from django.db import models
from pacientes.models import Paciente
from users.models import CustomUser

class Medicacion(models.Model):
    droga = models.CharField(max_length=200)
    dosis = models.CharField(max_length=200)
    presentacion = models.CharField(max_length=200)
    marca_recomendada = models.CharField(max_length=200, blank=True, null=True)
    cantidad_unidades = models.IntegerField()
    receta = models.ForeignKey('Receta', related_name='medicacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.droga} - {self.dosis}"

class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='recetas')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recetas')
    fecha = models.DateField(auto_now_add=True)
    firma_medica = models.CharField(max_length=200)
    fecha_ultimo_laboratorio = models.DateField()
    proxima_fecha_empadronamiento = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    viewed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Receta de {self.paciente.nombre} por {self.user.username}"

    def formatted_fecha(self):
        return self.fecha.strftime('%d-%m-%Y')

    def formatted_proxima_fecha_empadronamiento(self):
        return self.proxima_fecha_empadronamiento.strftime('%d-%m-%Y')

    def formatted_fecha_ultimo_laboratorio(self):
        return self.fecha_ultimo_laboratorio.strftime('%d-%m-%Y')