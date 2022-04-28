from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class Evento(models.Model):

    class Meta:
        verbose_name = _("Evento")
        verbose_name_plural = _("Eventos")
    
    nome = models.CharField(
        verbose_name=_("Nome"),
        unique = True,
        max_length=50,
        blank=False
    )

    descricao = models.TextField(
        verbose_name=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )

    data = models.DateTimeField(
        verbose_name=_("Data"),
        default=timezone.now
    )