from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import FormularioEvento
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Se importa el modelo Evento
from .models import Evento

# Create your views here.
@login_required
def lista_eventos(request):
    # Consulta los eventos ordenados por fecha de creación
    eventos = Evento.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'eventos/lista_eventos.html', {'eventos':eventos})

@login_required
def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})

@login_required
def evento_nuevo(request):
    if request.method == "POST":
        formulario = FormularioEvento(request.POST)
        if formulario.is_valid():
            evento = formulario.save(commit=False)
            evento.autor = request.user
            evento.fecha_creacion = timezone.now()
            evento.save()
            return redirect('detalle_evento', pk=evento.pk)
    else:
        formulario = FormularioEvento()
    return render(request, 'eventos/nuevo_evento.html', {'formulario': formulario})

@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        formulario = FormularioEvento(request.POST, instance=evento)
        if formulario.is_valid():
            evento = formulario.save(commit=False)
            evento.autor = request.user
            evento.save()
            return redirect('detalle_evento', pk=evento.pk)
    else:
        formulario = FormularioEvento(instance=evento)
    return render(request, 'eventos/nuevo_evento.html', {'formulario': formulario})

@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    evento.delete()
    return redirect('lista_eventos')
