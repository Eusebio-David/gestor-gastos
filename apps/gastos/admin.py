
# Register your models here.
from django.contrib import admin
from .models import Categoria, Presupuesto, Gasto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'monto_maximo', 'fecha_de_creacion', 'fecha_de_expiracion')
    list_filter = ('fecha_de_creacion', 'fecha_de_expiracion')

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'categoria', 'monto', 'fecha_creacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('descripcion',)
