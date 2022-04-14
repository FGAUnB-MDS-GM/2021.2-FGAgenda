from calendar import c
from unicodedata import name
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
from meta.models import Meta
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

# Create your views here.


class ToDoListView(CreateView):

    template_name='todolist.html'
    model = ToDoList
    form_class = ToDoForms
    
    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
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
        return reverse_lazy('todolist',
                            kwargs={'pk': self.get_meta_id()},
                            current_app='todolist')



def editar_tarefa(request, pk):
    conteudo_nova_tarefa = request.POST['conteudo']
    todolist = ToDoList.objects.get(pk=pk)
    #meta = Meta.objects.get(todolist=todolist)
    ToDoList.objects.filter(pk=pk).update(tarefa=conteudo_nova_tarefa)
    return HttpResponseRedirect(
        reverse_lazy('todolist', kwargs={'pk': todolist.meta.id }, 
                        current_app='todolist')
    )

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
    todolist = ToDoList.objects.get(pk=pk)
    ToDoList.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(
        reverse_lazy('todolist', kwargs={'pk': todolist.meta.id }, 
                        current_app='todolist')
    )

