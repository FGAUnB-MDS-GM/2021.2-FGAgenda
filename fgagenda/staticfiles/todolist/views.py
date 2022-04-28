from calendar import c
from unicodedata import name
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.core.exceptions import ValidationError
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
    #context_object_name = 'all_items'

    # ---------- Arrumar get_context_data para passar os objetos de todolist para o html ----------
    def get_context_data(self, **kwargs):
        context = super(ToDoListView, self).get_context_data(**kwargs)
        context['form'] = ToDoForms
        # self.kwargs['form'] = ToDoForms
        #context = {}
        #context['form'] = ToDoForms                       
        context['metas'] = Meta.objects.all()
        #context['all_items'] = ToDoList.objects.filter(meta=meta)
        context['all_items'] = ToDoList.objects.all()
        return context

    #def get_queryset(self):
    #   meta = Meta.objects.get(pk=self.kwargs['pk'])
    #   lista_tarefas = ToDoList.objects.filter(meta=meta)
    #    return lista_tarefas

    #form_class = ToDoForms
    success_url = reverse_lazy('todolist')


def adicionar_tarefa(request):
    conteudo_tarefa = request.POST['content']
    # if (x == NULL):
    #    raise ValidationError('Impossível adicionar tarefa vazia.')
    nova_tarefa = ToDoList(tarefa = conteudo_tarefa)
    nova_tarefa.save()
    return HttpResponseRedirect('/todolist/')


def editar_tarefa(request, pk):
    conteudo_nova_tarefa = request.POST['conteudo']
    ToDoList.objects.filter(pk=pk).update(tarefa=conteudo_nova_tarefa)
    return HttpResponseRedirect('/todolist/')


def deletar_tarefa(request, pk):
    ToDoList.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/todolist/') 

#class ListaTarefas(ListView):
#    template_name='todolist.html'
#    model = ToDoList
#    context_object_name = 'all_items'
#
#    def get_queryset(self):
#        lista_tarefas = ToDoList.objects.all()
#        return lista_tarefas
#
#    context = 'all_items'
#
#    success_url = reverse_lazy('todolist')
        

#class EditarTarefa(UpdateView):
#    template_name='todolist.html'
#    model = ToDoList
#    context_object_name = 'all_items'
#
#    fields = [
#        'tarefa'
#    ]
#    success_url = reverse_lazy('todolist')


#class ToDoListView(ListView):
    # template_name = "todolist.html"
    #model = ToDoList

    #def get(self, request):
        #return render(request, 'todolist.html.html', {})

    #success_url = reverse_lazy('todolist')


#def post_todolist(request):
#    return render(
#        request,
#        'todolist.html',
#        {'todolist':ToDoList.objects.all()}
#    )

#def criar_todo_list(request):
#    context = {}
#    context['form'] = ToDoForms
#    context['all_items'] = ToDoList.objects.all()
#    return render(request, 'todolist.html', context)
