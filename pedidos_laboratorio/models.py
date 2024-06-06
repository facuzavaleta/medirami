from django.db import models

class PedidoLaboratorio(models.Model):
    nombre_apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=20)
    obra_social = models.CharField(max_length=100)
    numero_afiliado = models.CharField(max_length=100)
    pedido = models.TextField()
    fecha = models.DateField()
    firma = models.CharField(max_length=200)
    codigo_identificacion = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Pedido de laboratorio de {self.nombre_apellido} - {self.fecha}"