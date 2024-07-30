from django.db import models
from pacientes.models import Paciente

class PedidoLaboratorio(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    pedido = models.TextField()
    fecha = models.DateField()
    firma = models.CharField(max_length=200)

    def __str__(self):
        return f"Pedido de laboratorio de {self.paciente.nombre} - {self.fecha}"