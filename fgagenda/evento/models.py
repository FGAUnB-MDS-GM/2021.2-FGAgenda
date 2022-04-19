from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Evento(models.Model):

    class Meta:
        verbose_name = _("Evento")
        verbose_name_plural = _("Eventos")
    
    nome = models.CharField(
        verbose_name=_("Nome"),
        unique = True,
        max_length=20,
        blank=False
    )

    descricao = models.TextField(
        verbose_name=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )

    dataInicio = models.DateTimeField(
        default=timezone.now
    )

    dataFim = models.DateTimeField(
        verbose_name=_("Data Fim"),
        blank=False,
        null=False,
    )

    def configura_data_inicio(self):
        self.dataInicio = timezone.now()
        self.save()
