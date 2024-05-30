from django.shortcuts import render
from rest_framework import viewsets
from .models import Medico, AsistenteMedico
from .serializers import MedicoSerializer, AsistenteMedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class AsistenteMedicoViewSet(viewsets.ModelViewSet):
    queryset = AsistenteMedico.objects.all()
    serializer_class = AsistenteMedicoSerializer
