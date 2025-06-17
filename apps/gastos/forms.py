from django import forms 
from .models import Gasto, Presupuesto

class GastoForm(forms.ModelForm):

    class Meta:
        model = Gasto
        fields = ['monto','descripcion','categoria']

class PresupuestoForm(forms.ModelForm):

    class Meta: 
        model = Presupuesto
        fields = ['monto_maximo', 'fecha_de_expiracion']
