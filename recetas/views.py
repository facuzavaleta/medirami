from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Receta
from .serializers import RecetaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    def perform_create(self, serializer):
        user = self.request.user
        paciente_id = self.request.data.get('paciente')

        if paciente_id is None:
            raise serializers.ValidationError({'error': 'El campo paciente es requerido.'})

        serializer.save(user=user, paciente_id=paciente_id)
