from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoLaboratorioViewSet

router = DefaultRouter()
router.register(r'', PedidoLaboratorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]