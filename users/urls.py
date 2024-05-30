from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, AsistenteMedicoViewSet

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'asistentes', AsistenteMedicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]