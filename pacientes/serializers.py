from rest_framework import serializers
from .models import Paciente
from users.models import CustomUser

class PacienteSerializer(serializers.ModelSerializer):
    edad = serializers.ReadOnlyField()
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='user')

    class Meta:
        model = Paciente
        fields = [
            'id', 'nombre', 'apellido', 'sexo', 'fecha_nacimiento',
            'obra_social', 'numero_afiliado', 'dni', 'provincia',
            'ciudad', 'medicacion', 'user_id', 'edad'
        ]