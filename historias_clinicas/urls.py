from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoriaClinicaViewSet

router = DefaultRouter()
router.register(r'', HistoriaClinicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
