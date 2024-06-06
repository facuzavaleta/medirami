from rest_framework import viewsets
from .models import PedidoLaboratorio
from .serializers import PedidoLaboratorioSerializer

class PedidoLaboratorioViewSet(viewsets.ModelViewSet):
    queryset = PedidoLaboratorio.objects.all()
    serializer_class = PedidoLaboratorioSerializer