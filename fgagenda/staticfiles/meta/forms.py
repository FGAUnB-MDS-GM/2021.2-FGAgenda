from django import forms
from .models import Meta as MetaModel
from django.utils.timezone import datetime, timedelta
from django.core.exceptions import ValidationError

class CriaMetaForm(forms.ModelForm):

    class Meta:
        dia_seguinte = datetime.today() + timedelta(days=1)
        dia_seguinte = dia_seguinte.replace(hour=0)
        model = MetaModel
        fields = [
            'nome',
            'descricao',
            'dataFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-meta-input",
                'placeholder': 'Nome da Meta'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-meta-input",
                'placeholder': 'Descrição'
            }),
            'dataFim': forms.DateTimeInput(attrs={
                'type': "datetime-local",          
                'class': "criar-meta-input",
                'min': dia_seguinte.strftime("%Y-%m-%dT%H:%M")
            }),
        }


class EditaMetaForm(forms.ModelForm):

    class Meta:
        dia_seguinte = datetime.today() + timedelta(days=1)
        dia_seguinte = dia_seguinte.replace(hour=0)
        model = MetaModel
        fields = [
            'nome',
            'descricao',
            'dataFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-meta-input",
                'placeholder': 'Nome da Meta'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-meta-input",
                'placeholder': 'Descrição'
            }),
            'dataFim': forms.DateTimeInput(attrs={  # Consertar "type" de dataFim, pois é possível criar
                'type': "datetime-local",           # uma Meta com data de um dia anterior!
                'class': "criar-meta-input",
                'min': dia_seguinte.strftime("%Y-%m-%dT%H:%M")
            }),
        }

    def clean(self):
        cleaned_data = super(EditaMetaForm, self).clean()
        
        return cleaned_data

    
