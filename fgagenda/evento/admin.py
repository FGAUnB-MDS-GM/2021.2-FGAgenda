from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Evento)
class PostAdmin(admin.ModelAdmin):
    list_display = ("nome", "dataInicio", "dataFim")
