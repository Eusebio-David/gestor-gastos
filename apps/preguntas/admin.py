from django.contrib import admin
from .models import PreguntasFrecuentes
# Register your models here.

@admin.register(PreguntasFrecuentes)
class PreguntasFrecuentesAdmin(admin.ModelAdmin):
    list_display = ('titulo','categoria', 'activo')