from django.urls import path
from .views import *

urlpatterns = [
  path('<int:pk>/', ToDoListView.as_view(template_name='todolist.html'), name="todolist"),
  path('editaTarefa/<int:pk>/', editar_tarefa, name='editar_tarefa'),
  path('deletaTarefa/<int:pk>/', deletar_tarefa, name="deletar_tarefa"), 
]

