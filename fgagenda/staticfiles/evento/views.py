from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *


class CreateEvento(CreateView):
    template_name='create_evento.html'
    model = Evento

    fields = [
        'nome',
        'descricao', 
        'data'
    ]
    success_url = reverse_lazy('create_evento.html')
