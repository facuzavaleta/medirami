from rest_framework import viewsets
from .models import HistoriaClinica
from .serializers import HistoriaClinicaSerializer

class HistoriaClinicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer