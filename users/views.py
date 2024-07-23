from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework import viewsets

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user = CustomUser.objects.get(username=serializer.validated_data['username'])
        tokens = serializer.validated_data
        response_data = {
            "access": tokens['access'],
            "refresh": tokens['refresh'],
            "user_id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return Response(response_data, status=status.HTTP_200_OK)

class MyTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)
