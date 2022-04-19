from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *


class CriaEvento(CreateView):
    template_name = 'criar_evento.html'
    model = Evento
    form_class = CriaEventoForm

    success_url = reverse_lazy('inicio')
    

class EditaEvento(UpdateView):
    template_name='editar_evento.html'
    model = Evento
    form_class = EditaEventoForm
    
    success_url = reverse_lazy('inicio')


class DeletaEvento(DeleteView):
    template_name = 'deletar_evento.html'
    queryset = Evento.objects.all()
    
    success_url = reverse_lazy('inicio')
    