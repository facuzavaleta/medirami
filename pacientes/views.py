from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        user_id = self.request.query_params.get('id', None)
        if user_id is not None:
            try:
                user_id = int(user_id)
                queryset = queryset.filter(user_id=user_id)
            except ValueError:
                print(f"Error: id incorrecto")
        return queryset