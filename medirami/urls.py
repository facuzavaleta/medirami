from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('pacientes.urls')),
    path('api/historias_clinicas/', include('historias_clinicas.urls')),
]