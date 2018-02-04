from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Clase Evento
class Evento(models.Model):

    # Definicion atributos

    nombre = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)

    # Diferentes Categorias

    CONFERENCIA = 'CF'
    SEMINARIO = 'SM'
    CONGRESO = 'CN'
    CURSO = 'CR'

    CATEGORIAS = (
        (CONFERENCIA, 'Conferencia'),
        (SEMINARIO, 'Seminario'),
        (CONGRESO, 'Congreso'),
        (CURSO, 'Curso'),
    )
    categoria = models.CharField(max_length=2,
                                choices=CATEGORIAS,
                                default=CONFERENCIA)

    # Tipos de Evento

    PRESENCIAL = 'PR'
    VIRTUAL = 'VR'

    TIPO_EVENTO = (
        (PRESENCIAL, 'Presencial'),
        (VIRTUAL, 'Virtual'),
    )
    tipo_evento = models.CharField(max_length=2,
                                choices=TIPO_EVENTO,
                                default=PRESENCIAL)

    def crear_evento(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
