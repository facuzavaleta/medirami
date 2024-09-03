from django.db import models
from pacientes.models import Paciente
from users.models import CustomUser

class Medicacion(models.Model):
    droga = models.CharField(max_length=200)
    presentacion = models.CharField(max_length=200)
    marca_recomendada = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.droga} - {self.presentacion} - {self.marca_recomendada}"
        

class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='recetas')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recetas')
    fecha = models.DateField(auto_now_add=True)
    firma_medica = models.CharField(max_length=200)
    fecha_ultimo_laboratorio = models.DateField()
    proxima_fecha_empadronamiento = models.DateField()
    observaciones = models.TextField(blank=True, null=True)
    codigo_de_receta = models.CharField(max_length=20, blank=True, editable=False)

    def __str__(self):
        return f"Receta de {self.paciente.nombre} por {self.user.username}"

    def formatted_fecha(self):
        return self.fecha.strftime('%d-%m-%Y')

    def formatted_proxima_fecha_empadronamiento(self):
        return self.proxima_fecha_empadronamiento.strftime('%d-%m-%Y')

    def formatted_fecha_ultimo_laboratorio(self):
        return self.fecha_ultimo_laboratorio.strftime('%d-%m-%Y')


class RecetaMedicacion(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='receta_medicaciones')
    medicacion = models.ForeignKey(Medicacion, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=200)
    cantidad_unidades = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.medicacion.droga} - Dosis: {self.dosis}, Cantidad: {self.cantidad_unidades}"
