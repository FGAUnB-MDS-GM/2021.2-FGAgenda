from django.urls import path
from .views import *

urlpatterns = [
  path('meta/<int:pk>/', ToDoListMetaView.as_view(template_name='todolist.html'), name="todolist_meta"),
  path('evento/<int:pk>/', ToDoListEventoView.as_view(template_name='todolist.html'), name="todolist_evento"),
  path('editaTarefa/<int:pk>/', editar_tarefa, name='editar_tarefa'),
  path('deletaTarefa/<int:pk>/', deletar_tarefa, name="deletar_tarefa"), 
]

