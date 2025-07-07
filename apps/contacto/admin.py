from django.contrib import admin
from .models import InformacionContacto
# Register your models here.



@admin.register(InformacionContacto)
class InformacionContactoAdmin(admin.ModelAdmin):
    pass
