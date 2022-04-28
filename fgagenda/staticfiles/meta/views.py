from urllib.request import Request
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from django.utils.timezone import datetime
from .models import *
from .forms import *
from todolist.forms import *

class CriaMeta(CreateView):
    template_name = 'criar_meta.html'
    model = Meta
    form_class = CriaMetaForm

    success_url = reverse_lazy('inicio')
    

class EditaMeta(UpdateView):
    template_name='editar_meta.html'
    model = Meta
    form_class = EditaMetaForm
    
    success_url = reverse_lazy('inicio')


class DeletaMeta(DeleteView):
    template_name = 'deletar_meta.html'
    queryset = Meta.objects.all()
    
    success_url = reverse_lazy('inicio')