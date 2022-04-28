from django.db import models
from django.core.validators import RegexValidator
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

    dia = models.DateField(
        verbose_name=_("Dia"),
        blank=False,
        null=False
    )

    frequencia = models.CharField(max_length=35)

    horaInicio = models.TimeField(
        verbose_name=_("Hora Inicio"),
        blank=False,
        null=False
    )

    horaFim = models.TimeField(
        verbose_name=_("Hora Fim"),
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.nome


class Aula(models.Model):

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

    horarioAula = models.CharField(
        verbose_name=_("Horário Aula UnB"),
        max_length=6,
        blank=False
    )

    def __str__(self):
        return self.nome
