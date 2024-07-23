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
            'ciudad', 'medicacion', 'edad', 'user_id'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('user_id', None)
        return representation