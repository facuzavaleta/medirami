from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, MyTokenObtainPairView, MyTokenRefreshView, CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]