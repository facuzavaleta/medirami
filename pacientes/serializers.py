from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    edad = serializers.ReadOnlyField()

    class Meta:
        model = Paciente
        fields = [
            'id', 'nombre', 'apellido', 'sexo', 'fecha_nacimiento',
            'obra_social', 'numero_afiliado', 'dni', 'provincia',
            'ciudad', 'medicacion', 'historia_clinica', 'edad'
        ]