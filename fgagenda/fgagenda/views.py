from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from meta.models import Meta
from evento.models import Evento, Aula

class BaseView(TemplateView):
  pass

class Inicio(ListView):
    template_name = 'pagina-principal.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['metas'] = Meta.objects.all()
        context['eventos'] = Evento.objects.all()
        context['aulas'] = Aula.objects.all()
        return context   
    
    def get_queryset(self):
        metas = Meta.objects.all()
        eventos = Evento.objects.all()
        aulas = Aula.objects.all()

        queryset = []

        for meta in metas:
            queryset.append({
                'meta': meta, 
            })

        for evento in eventos:
            queryset.append({
                'evento': evento, 
            }) 

        for aula in aulas:
            queryset.append({
                'evento': aula, 
            })

        return queryset 

    """ def get_queryset(self):
        eventos = Evento.objects.all()

        queryset = []

        for evento in eventos:
            queryset.append({
                'evento': evento, 
            })

        return queryset """

class Selecionar(TemplateView):
    pass
