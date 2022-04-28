from calendar import c
from unicodedata import name
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, resolve
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
from meta.models import Meta
from evento.models import Evento
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

# Create your views here.


class ToDoListMetaView(CreateView):

    template_name='todolist.html'
    model = ToDoList
    form_class = ToDoMetaForms
    
    def get_context_data(self, **kwargs):
        context = super(ToDoListMetaView, self).get_context_data(**kwargs)
        meta = Meta.objects.get(pk=self.kwargs['pk'])
        context['meta'] = meta
        context['all_items'] = ToDoList.objects.filter(meta=meta)
        #context['all_items'] = ToDoList.objects.filter(meta=meta)
        return context   

    def get_queryset(self):
        meta = Meta.objects.get(pk=self.kwargs['pk'])
        todolist = ToDoList.objects.filter(meta=meta)
        return todolist
    
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def get_meta_id(self):
        meta = Meta.objects.get(pk=self.kwargs['pk'])
        meta_id = meta.id
        return meta_id
    
    def get_success_url(self):
        """ Return the URL to redirect to after processing a valid form. """
        return reverse_lazy('todolist_meta',
                            kwargs={'pk': self.get_meta_id()},
                            current_app='todolist')


class ToDoListEventoView(CreateView):

    template_name='todolist.html'
    model = ToDoListEvento
    form_class = ToDoEventoForms
    
    def get_context_data(self, **kwargs):
        context = super(ToDoListEventoView, self).get_context_data(**kwargs)
        evento = Evento.objects.get(pk=self.kwargs['pk'])
        context['all_items'] = ToDoListEvento.objects.filter(evento=evento)
        #context['all_items'] = ToDoList.objects.filter(meta=meta)
        return context   

    def get_queryset(self):
        evento = Evento.objects.get(pk=self.kwargs['pk'])
        todolist = ToDoListEvento.objects.filter(evento=evento)
        return todolist
    
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def get_evento_id(self):
        evento = Evento.objects.get(pk=self.kwargs['pk'])
        evento_id = evento.id
        return evento_id
    
    def get_success_url(self):
        """ Return the URL to redirect to after processing a valid form. """
        return reverse_lazy('todolist_evento',
                            kwargs={'pk': self.get_evento_id()},
                            current_app='todolist')


def editar_tarefa(request, pk):
    conteudo_nova_tarefa = request.POST['conteudo']

    try:
        todolist_de_meta = ToDoList.objects.get(pk=pk)
    except:
        todolist_de_evento = ToDoListEvento.objects.get(pk=pk)
        todolist_de_evento.tarefa = conteudo_nova_tarefa
        todolist_de_evento.save()
        pk = todolist_de_evento.evento.id
        todolist_url = 'todolist_evento'
    else:
        todolist_de_meta.tarefa = conteudo_nova_tarefa
        todolist_de_meta.save()
        pk = todolist_de_meta.meta.id
        todolist_url = 'todolist_meta'
    finally:
        return HttpResponseRedirect(
        reverse_lazy(todolist_url, kwargs={'pk': pk }, 
                        current_app='todolist')
    )

    """ #meta = Meta.objects.get(todolist=todolist)
    if ToDoList.objects.filter(meta=todolist.meta).exists():
        ToDoList.objects.filter(pk=pk).update(tarefa=conteudo_nova_tarefa)
        pk = todolist.meta.id
        todolist_url = 'todolist_meta'
    else:
        ToDoListEvento.objects.filter(pk=pk).update(tarefa=conteudo_nova_tarefa)
        pk = todolist.evento.id
        todolist_url = 'todolist_evento'

    return HttpResponseRedirect(
        reverse_lazy(todolist_url, kwargs={'pk': pk }, 
                        current_app='todolist')
    ) """

    """ return reverse_lazy('todolist', 
                        kwargs={'pk': meta_pk}, 
                        current_app='todolist') 
             
    HttpResponseRedirect(
                reverse_lazy('todolist', 
                            kwargs={'meta_pk': meta_pk}, 
                            current_app='todolist')
            )
    """

def deletar_tarefa(request, pk):
    """ todolist = ToDoList.objects.get(pk=pk)
    ToDoList.objects.filter(pk=pk).delete() """

    try:
        todolist_de_meta = ToDoList.objects.get(pk=pk)
    except:
        todolist_de_evento = ToDoListEvento.objects.get(pk=pk)
        pk = todolist_de_evento.evento.id
        todolist_url = 'todolist_evento'
        todolist_de_evento.delete()
    else:
        pk = todolist_de_meta.meta.id
        todolist_url = 'todolist_meta'
        todolist_de_meta.delete()
    finally:
        return HttpResponseRedirect(
        reverse_lazy(todolist_url, kwargs={'pk': pk }, 
                        current_app='todolist')
    )
