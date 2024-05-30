from rest_framework import serializers
from .models import CustomUser, Medico, AsistenteMedico

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_medico', 'is_asistente', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            is_medico=validated_data.get('is_medico', False),
            is_asistente=validated_data.get('is_asistente', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class MedicoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Medico
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUserSerializer.create(CustomUserSerializer(), validated_data=user_data)
        medico, created = Medico.objects.update_or_create(user=user)
        return medico
    
class AsistenteMedicoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    medico = serializers.PrimaryKeyRelatedField(queryset=Medico.objects.all())

    class Meta:
        model = AsistenteMedico
        fields = ['user', 'medico']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        medico_data = validated_data.pop('medico')
        user = CustomUserSerializer.create(CustomUserSerializer(), validated_data=user_data)
        asistente_medico, created = AsistenteMedico.objects.update_or_create(user=user, medico=medico_data)
        return asistente_medico