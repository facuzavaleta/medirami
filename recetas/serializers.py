from rest_framework import serializers
from .models import Receta, Medicacion, RecetaMedicacion

class MedicacionBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicacion
        fields = ['droga', 'presentacion', 'marca_recomendada']

class RecetaMedicacionSerializer(serializers.ModelSerializer):
    medicacion = MedicacionBaseSerializer()

    class Meta:
        model = RecetaMedicacion
        fields = ['medicacion', 'dosis', 'cantidad_unidades']

class RecetaSerializer(serializers.ModelSerializer):
    receta_medicaciones = RecetaMedicacionSerializer(many=True)

    class Meta:
        model = Receta
        fields = [
            'id', 'paciente', 'user', 'firma_medica',
            'fecha_ultimo_laboratorio', 'proxima_fecha_empadronamiento',
            'observaciones', 'receta_medicaciones'
        ]

    def create(self, validated_data):
        receta_medicaciones_data = validated_data.pop('receta_medicaciones')
        receta = Receta.objects.create(**validated_data)

        for medicacion_item in receta_medicaciones_data:
            medicacion_data = medicacion_item.pop('medicacion')
            # Buscar o crear la instancia de Medicacion
            medicacion, created = Medicacion.objects.get_or_create(
                droga=medicacion_data['droga'],
                presentacion=medicacion_data['presentacion'],
                marca_recomendada=medicacion_data.get('marca_recomendada')
            )

            # Crear la relación de Receta con Medicacion
            RecetaMedicacion.objects.create(
                receta=receta,
                medicacion=medicacion,
                dosis=medicacion_item['dosis'],
                cantidad_unidades=medicacion_item['cantidad_unidades']
            )

        return receta

    def update(self, instance, validated_data):
        receta_medicaciones_data = validated_data.pop('receta_medicaciones')

        # Actualizar los campos de la receta
        instance.paciente = validated_data.get('paciente', instance.paciente)
        instance.user = validated_data.get('user', instance.user)
        instance.firma_medica = validated_data.get('firma_medica', instance.firma_medica)
        instance.fecha_ultimo_laboratorio = validated_data.get('fecha_ultimo_laboratorio', instance.fecha_ultimo_laboratorio)
        instance.proxima_fecha_empadronamiento = validated_data.get('proxima_fecha_empadronamiento', instance.proxima_fecha_empadronamiento)
        instance.observaciones = validated_data.get('observaciones', instance.observaciones)
        instance.save()

        # Eliminar las medicaciones actuales
        instance.receta_medicaciones.all().delete()

        for medicacion_item in receta_medicaciones_data:
            medicacion_data = medicacion_item.pop('medicacion')
            # Buscar o crear la instancia de Medicacion
            medicacion, created = Medicacion.objects.get_or_create(
                droga=medicacion_data['droga'],
                presentacion=medicacion_data['presentacion'],
                marca_recomendada=medicacion_data.get('marca_recomendada')
            )

            # Crear la nueva relación de Receta con Medicacion
            RecetaMedicacion.objects.create(
                receta=instance,
                medicacion=medicacion,
                dosis=medicacion_item['dosis'],
                cantidad_unidades=medicacion_item['cantidad_unidades']
            )

        return instance