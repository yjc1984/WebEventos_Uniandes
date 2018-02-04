from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Se importa el modelo Evento
from .models import Evento

# Create your views here.
def lista_eventos(request):
    # Consulta los eventos ordenados por fecha de creación
    eventos = Evento.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'eventos/lista_eventos.html', {'eventos':eventos})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})
