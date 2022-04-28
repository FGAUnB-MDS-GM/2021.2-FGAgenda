from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Meta)

@admin.register(Meta)
class PostAdmin(admin.ModelAdmin):
    list_display = ("nome", "dataInicio", "dataFim")