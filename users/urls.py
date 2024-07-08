from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, MyTokenObtainPairView, MyTokenRefreshView, CustomUserViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'user', CustomUserViewSet, basename='user')
=======
router.register(r'users', CustomUserViewSet, basename='user')
>>>>>>> 6464133e9b90b39c9f6db404a72bd90bdd6c0c9e

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]