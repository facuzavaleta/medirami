from django.db import models
from users.models import CustomUser

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    PROVINCIAS_CHOICES = [
    ('Buenos Aires', 'Buenos Aires'),
    ('CABA', 'Ciudad Autónoma de Buenos Aires'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'),
    ('Río Negro', 'Río Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucumán', 'Tucumán'),
]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pacientes')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    obra_social = models.CharField(max_length=100)
    numero_afiliado = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    provincia = models.CharField(max_length=100, choices=PROVINCIAS_CHOICES)
    ciudad = models.CharField(max_length=100)
    medicacion = models.TextField(blank=True, null=True)

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