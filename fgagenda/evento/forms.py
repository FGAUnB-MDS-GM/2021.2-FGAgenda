from django import forms
from .models import Evento as EventoModel
from django.utils.timezone import datetime, timedelta
from django.core.exceptions import ValidationError

class CriaEventoForm(forms.ModelForm):

    class Meta:
        dia_seguinte = datetime.today() + timedelta(days=1)
        dia_seguinte = dia_seguinte.replace(hour=0)
        model = EventoModel
        fields = [
            'nome',
            'descricao',
            'dataFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Nome do Evento'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Descrição'
            }),
            'dataFim': forms.DateTimeInput(attrs={
                'type': "datetime-local",          
                'class': "criar-evento-input",
                'min': dia_seguinte.strftime("%Y-%m-%dT%H:%M")
            }),
        }

class EditaEventoForm(forms.ModelForm):

    class Evento:
        dia_seguinte = datetime.today() + timedelta(days=1)
        dia_seguinte = dia_seguinte.replace(hour=0)
        model = EventoModel
        fields = [
            'nome',
            'descricao',
            'dataFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Nome do Evento'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Descrição'
            }),
            'dataFim': forms.DateTimeInput(attrs={ 
                'type': "datetime-local",           
                'class': "criar-evento-input",
                'min': dia_seguinte.strftime("%Y-%m-%dT%H:%M")
            }),
        }

    def clean(self):
        cleaned_data = super(EditaEventoForm, self).clean()
        
        return cleaned_data
