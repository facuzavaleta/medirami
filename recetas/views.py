from rest_framework import viewsets
from .models import Receta
from .serializers import RecetaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    def perform_create(self, serializer):
        paciente_tipo = self.request.data.get('paciente_tipo')
        if paciente_tipo == 'existente':
            paciente_id = self.request.data.get('paciente_existente')
        elif paciente_tipo == 'nuevo':
            paciente_id = None
        
        user = self.request.user
        serializer.save(user=user, paciente_existente_id=paciente_id)