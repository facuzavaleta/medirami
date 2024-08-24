from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet

router = DefaultRouter()
router.register(r'', RecetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/detail/', RecetaViewSet.as_view({'get': 'detail'}), name='receta-detail'),
]