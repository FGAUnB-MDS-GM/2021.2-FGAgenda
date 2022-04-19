from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
  path('', CriaEvento.as_view(template_name='criar_evento.html'), name="criar_evento"),
  path('editar/<int:pk>/', EditaEvento.as_view(template_name='editar_evento.html'), name='editar_evento'),
  path('deletar/<int:pk>/', DeletaEvento.as_view(template_name='deletar_evento.html'), name="deletar_evento")
]