from django import forms

from .models import Evento

class FormularioEvento(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('nombre','lugar','direccion','fecha_inicio','fecha_fin','categoria','tipo_evento')
