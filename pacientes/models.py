from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    PROVINCIAS_CHOICES = [
    ('Buenos Aires', 'Buenos Aires'),
    ('CABA', 'Ciudad Autonoma de Buenos Aires'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Cordoba', 'Cordoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Rios', 'Entre Rios'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquen', 'Neuquen'),
    ('Rio Negro', 'Rio Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'),
    ('Tucuman', 'Tucuman'),
]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pacientes')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(120)])
    obra_social = models.CharField(max_length=100)
    numero_afiliado = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    provincia = models.CharField(max_length=100, choices=PROVINCIAS_CHOICES)
    ciudad = models.CharField(max_length=100)
    medicacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'