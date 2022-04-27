from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
  path('', CriaEvento.as_view(template_name='criar_evento.html'), name="criar_evento"),
  path('editar/<int:pk>/', EditaEvento.as_view(template_name='editar_evento.html'), name='editar_evento'),
  path('deletar/<int:pk>/', DeletaEvento.as_view(template_name='deletar_evento.html'), name="deletar_evento"),
  path('aula/', CriaAula.as_view(template_name='criar_aula.html'), name="criar_aula"),
  path('aula/editar/<int:pk>/', EditaAula.as_view(template_name='editar_aula.html'), name='editar_aula'),
  path('aula/deletar/<int:pk>/', DeletaAula.as_view(template_name='deletar_aula.html'), name="deletar_aula"),
  path('selecionar/', Selecionar.as_view(template_name="evento-aula.html"), name="evento-aula"),
]