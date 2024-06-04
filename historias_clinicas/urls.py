from django.urls import path
from .views import HistoriaClinicaListCreateView, HistoriaClinicaDetailView

urlpatterns = [
    path('', HistoriaClinicaListCreateView.as_view(), name='historias_clinicas-list-create'),
    path('<int:pk>/', HistoriaClinicaDetailView.as_view(), name='historias_clinicas-detail'),
]