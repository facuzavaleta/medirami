from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'is_medico', 'is_verified', 
            'supervisor', 'password', 'first_name', 'last_name'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_medico=validated_data.get('is_medico', False),
            is_verified=validated_data.get('is_verified', False),
            supervisor=validated_data.get('supervisor', None),  # Nuevo campo
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
