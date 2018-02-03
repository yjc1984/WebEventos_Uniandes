from django.contrib import admin
# Se importa el modelo Evento
from .models import Evento

# Se registra en modelo Evento en la pagina administrador
admin.site.register(Evento)
