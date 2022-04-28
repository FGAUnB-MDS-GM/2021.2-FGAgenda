from django import forms
from .models import *
from django.core.exceptions import ValidationError
##from django.forms import *

""" class CreateEvento(forms.ModelForm):

  class Meta:
    model = Evento
    fields = [
        'nome',
        'descricao',
        'data'
    ]
    widgets = {
      'product_type': forms.CharField(attrs={
        'class': "create-evento-input",
        'placeholder': 'Nome'
      }),
      'descricao': forms.Textarea(attrs={
        'class': "create-evento-input",
        'placeholder': 'Descrição'
      }),
      'data': forms.DateTimeField(attrs={
        'class': "create-evento-input",
        'placeholder': 'Data'
      }),
    } """
