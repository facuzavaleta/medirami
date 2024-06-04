from rest_framework import generics
from .models import HistoriaClinica
from .serializers import HistoriaClinicaSerializer

class HistoriaClinicaListCreateView(generics.ListCreateAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer

class HistoriaClinicaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer