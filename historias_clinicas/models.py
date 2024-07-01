from django.db import models
from pacientes.models import Paciente

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    ultima_medicacion = models.CharField(max_length=255)
    dosis_diaria = models.CharField(max_length=255)
    app = models.TextField(verbose_name='Antecedentes Patológicos Personales')
    aqx = models.TextField(verbose_name='Antecedentes Quirúrgicos')
    complicaciones = models.TextField(verbose_name='Complicaciones (agudas y/o crónicas)')
    actividad_fisica = models.TextField()
    act_laboral = models.TextField(verbose_name='Actividad Laboral')
    clinica = models.TextField()
    amg = models.TextField(verbose_name='Automonitoreo Glucémico')
    laboratorio = models.TextField()
    interconsultas = models.TextField()
    conducta = models.TextField()

    def __str__(self):
        return f"Historia Clinica de {self.paciente.nombre} {self.paciente.apellido}"