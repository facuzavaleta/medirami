from django.db import models

class RecetaQR(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo_qr = models.ImageField(upload_to='codigos_qr/', blank=True)

    def __str__(self):
        return self.nombre_paciente