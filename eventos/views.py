from django.shortcuts import render
from django.utils import timezone
# Se importa el modelo Evento
from .models import Evento

# Create your views here.
def lista_eventos(request):
    # Consulta los eventos ordenados por fecha de creación
    eventos = Evento.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'eventos/lista_eventos.html', {'eventos':eventos})
