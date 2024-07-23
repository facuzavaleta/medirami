# from rest_framework import serializers
# from .models import Receta

# class RecetaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Receta
#         fields = '__all__'
from rest_framework import serializers
from .models import Receta, Medicacion

class MedicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicacion
        fields = ['droga', 'dosis', 'presentacion', 'marca_recomendada', 'cantidad_unidades']

class RecetaSerializer(serializers.ModelSerializer):
    medicacion = MedicacionSerializer(many=True)

    class Meta:
        model = Receta
        fields = [
            'id','paciente', 'user', 'medicacion', 'firma_medica',
            'fecha_ultimo_laboratorio', 'proxima_fecha_empadronamiento', 'observaciones'
        ]

    def create(self, validated_data):
        medicacion_data = validated_data.pop('medicacion')
        receta = Receta.objects.create(**validated_data)
        for med_data in medicacion_data:
            Medicacion.objects.create(receta=receta, **med_data)
        return receta

    def update(self, instance, validated_data):
        medicacion_data = validated_data.pop('medicacion')
        instance.paciente = validated_data.get('paciente', instance.paciente)
        instance.user = validated_data.get('user', instance.user)
        instance.firma_medica = validated_data.get('firma_medica', instance.firma_medica)
        instance.fecha_ultimo_laboratorio = validated_data.get('fecha_ultimo_laboratorio', instance.fecha_ultimo_laboratorio)
        instance.proxima_fecha_empadronamiento = validated_data.get('proxima_fecha_empadronamiento', instance.proxima_fecha_empadronamiento)
        instance.observaciones = validated_data.get('observaciones', instance.observaciones)
        instance.save()

        instance.medicacion.all().delete()
        for med_data in medicacion_data:
            Medicacion.objects.create(receta=instance, **med_data)

        return instance