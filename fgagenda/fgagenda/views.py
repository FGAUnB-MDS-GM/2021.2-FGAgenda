from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from meta.models import Meta

class BaseView(TemplateView):
  pass

class Inicio(ListView):
    template_name = 'pagina-principal.html'
    #model = ProductType
        
    def get_queryset(self):
        metas = Meta.objects.all()

        queryset = []

        for meta in metas:
            queryset.append({
                'meta': meta, 
            })

        return queryset

class Selecionar(TemplateView):
    pass
