from django.urls import path
from .views import *

urlpatterns = [
  path('', ToDoListView.as_view(template_name='todolist.html'), name="todolist"),
  #path('listaTarefas/', ListaTarefas.as_view(template_name='todolist.html'), name="listar_todolist"),
  path('editaTarefa/<int:pk>/', editar_tarefa, name='editar_tarefa'),
  path('adicionaTarefa/', adicionar_tarefa, name="adicionar_tarefa"),
  path('deletaTarefa/<int:pk>/', deletar_tarefa, name="deletar_tarefa"), 
  #path('editaTarefa/<int:pk>/', editar_tarefa, name="editar_tarefa"),
]

