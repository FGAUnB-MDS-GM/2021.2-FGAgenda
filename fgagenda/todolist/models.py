from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from meta.models import Meta as MetaModel
from evento.models import Evento

class ToDoList(models.Model):
    """
    Abstract class that represents class 'Component' in Composite Pattern.
    """
    
    class Meta:
        verbose_name = _("Lista de Tarefa")
        verbose_name_plural = _("Lista de Tarefas")
    
    meta = models.ForeignKey(
        MetaModel,
        related_name="Meta",
        verbose_name=_("Meta"),
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    
    tarefa = models.CharField(
        verbose_name=_("Tarefa"),
        max_length=50,
        editable=True,
        blank=False,
        null=True
    )

class ToDoListEvento(models.Model):
    """
    Abstract class that represents class 'Component' in Composite Pattern.
    """
    
    class Meta:
        verbose_name = _("Lista de Tarefa")
        verbose_name_plural = _("Lista de Tarefas")
    
    evento = models.ForeignKey(
        Evento,
        related_name="Evento",
        verbose_name=_("Evento"),
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    
    tarefa = models.CharField(
        verbose_name=_("Tarefa"),
        max_length=50,
        editable=True,
        blank=False,
        null=True
    )