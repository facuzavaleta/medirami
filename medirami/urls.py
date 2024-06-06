from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/pacientes/', include('pacientes.urls')),
    path('api/historias_clinicas/', include('historias_clinicas.urls')),
    path('api/recetas/', include('recetas.urls')),
    path('api/pedidos_laboratorio/', include('pedidos_laboratorio.urls')),
]
