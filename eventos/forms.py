from django import forms

from .models import Evento
from django.contrib.auth.models import User

class FormularioEvento(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('nombre','lugar','direccion','fecha_inicio','fecha_fin','categoria','tipo_evento')
