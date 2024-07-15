from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
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
        serializer.save(user=user, paciente_id=paciente_id)

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        receta = self.get_object()
        if receta.viewed:
            return Response({"detail": "Esta receta ya fue utilizada"}, status=status.HTTP_400_BAD_REQUEST)
        if receta.is_expired():
            return Response({"detail": f"La receta debió usarse antes de {receta.fecha + receta.tiempo_de_vida}"}, status=status.HTTP_400_BAD_REQUEST)
        
        receta.viewed = True
        receta.save()
        serializer = self.get_serializer(receta)
        return Response(serializer.data)