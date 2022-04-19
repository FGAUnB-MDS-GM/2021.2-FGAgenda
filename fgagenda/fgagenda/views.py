from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from meta.models import Meta
from evento.models import Evento

class BaseView(TemplateView):
  pass

class Inicio(ListView):
    template_name = 'pagina-principal.html'
        
    def get_queryset(self):
        metas = Meta.objects.all()

        queryset = []

        for meta in metas:
            queryset.append({
                'meta': meta, 
            })

        return queryset

    def get_queryset(self):
        eventos = Evento.objects.all()

        queryset = []

        for evento in eventos:
            queryset.append({
                'evento': evento, 
            })

        return queryset

class Selecionar(TemplateView):
    pass
