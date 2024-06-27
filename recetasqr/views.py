from django.shortcuts import render, redirect, get_object_or_404
from .models import RecetaQR
from .utils import generar_codigo_qr

def crear_receta(request):
    if request.method == 'POST':
        nombre_paciente = request.POST.get('nombre_paciente')
        descripcion = request.POST.get('descripcion')

        # Crear la instancia de RecetaQR
        receta = RecetaQR(nombre_paciente=nombre_paciente, descripcion=descripcion)
        receta.save()

        # URL de redirección deseada (en este caso, google.com)
        url_redireccion = 'https://www.google.com/'

        # Generar el código QR con la URL de redirección
        receta.codigo_qr = generar_codigo_qr(url_redireccion)
        receta.save()

        return redirect('detalle_receta', pk=receta.pk)

    return render(request, 'recetasqr/crear_receta.html')

def detalle_receta(request, pk):
    receta = get_object_or_404(RecetaQR, pk=pk)
    return render(request, 'recetasqr/detalle_receta.html', {'receta': receta})