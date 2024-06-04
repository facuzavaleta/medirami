from django.db import models

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    obra_social = models.CharField(max_length=100)
    numero_afiliado = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    medicacion = models.TextField(blank=True, null=True)
    historia_clinica = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    @property
    def edad(self):
        import datetime
        today = datetime.date.today()
        age = today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
        return age