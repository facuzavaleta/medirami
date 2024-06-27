from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/pacientes/', include('pacientes.urls')),
    path('api/historias_clinicas/', include('historias_clinicas.urls')),
    path('api/recetas/', include('recetas.urls')),
    path('api/pedidos_laboratorio/', include('pedidos_laboratorio.urls')),
    path('recetasqr/', include('recetasqr.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)