from rest_framework import serializers
from .models import PedidoLaboratorio

class PedidoLaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoLaboratorio
        fields = '__all__'