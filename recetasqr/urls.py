from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_receta, name='crear_receta'),
    path('detalle/<int:pk>/', views.detalle_receta, name='detalle_receta'),
]