from django.db import models
from pacientes.models import Paciente  # Asegurate de importar correctamente el modelo Paciente
from users.models import CustomUser

class PedidoLaboratorio(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='pedidos_laboratorio')
    pedido = models.TextField()
    fecha = models.DateField()
    firma = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pedidos_firmados')
    codigo_identificacion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Pedido de laboratorio de {self.paciente.nombre} {self.paciente.apellido} - {self.fecha}"