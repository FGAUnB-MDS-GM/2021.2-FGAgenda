from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
  path('', CreateEvento.as_view(template_name="create_evento.html"), name="create_evento"),
]