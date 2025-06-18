from django import forms 
from .models import Gasto, Presupuesto, Categoria
from django.utils import timezone
from django.db import models

class GastoForm(forms.ModelForm):

    class Meta:
        model = Gasto
        fields = ['monto','descripcion','categoria','metodo_pago', 'nota_adicionales','archivo_adjunto']

        widgets = {
            'metodo_pago': forms.Select(attrs={
                'id': 'payment-method',
                'class': 'block w-full pl-10 pr-10 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget appearance-none',
            }),
            'nota_adicionales': forms.Textarea(attrs={
                'id': 'edit-notes',
                'rows': 3,
                'class': 'block w-full px-3 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-goodbudget focus:border-goodbudget resize-none'
            })
        }
    
    
    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)

    def clean(self):

        """
        Validamos si existe el usuario asignado, pero para que esto no nos de error, en la vista CrarGasto sobreescribimos el método get_form_kwargs
        luego filtramos los gastos creados anteriormente para verificar si hay monto disponible, así prodemos saber si el gasto que se esta por efectuar puede ser posible o no.
        
        """
        cleaned_data = super().clean()
        if not self.usuario:
            raise forms.ValidationError("El usuario no está definido.")
        
        # validación del presupuesto
        hoy = timezone.now().date()
        try:
            presupuesto = Presupuesto.objects.get(
                usuario=self.usuario,
                fecha_de_creacion__lte=hoy,#verificamos que la fecha de creacion sea menor o igual que a la de hoy
                fecha_de_expiracion__gte=hoy #verificamos que la fecha de expiracion sea mayor o igual a la de hoy. 
            )
        except Presupuesto.DoesNotExist:
            raise forms.ValidationError("No hay presupuesto vigente para este usuario.")
        
        monto = cleaned_data.get("monto")
        if monto is not None:
            gastos_previos = Gasto.objects.filter(
                usuario=self.usuario,
                fecha_creacion__gte=presupuesto.fecha_de_creacion,
                fecha_creacion__lte=presupuesto.fecha_de_expiracion
            )
            total = gastos_previos.aggregate(total=models.Sum('monto'))['total'] or 0

            disponible = presupuesto.monto_maximo - total

            #Verificamos que el gasto no supere el monto dispobible
            if monto > disponible:
                raise forms.ValidationError(f"Este gasto supera el presupuesto disponible (${disponible}).")


class PresupuestoForm(forms.ModelForm):

    class Meta: 
        model = Presupuesto
        fields = ['monto_maximo', 'fecha_de_expiracion']

class CategoriaForm(forms.ModelForm):
    """
    El método sobreescribe la validación del campo nombre dentro del formulario.
    Se ejecuta automáticamente al hacer form.is_valid()
    Luego obtenemos el valor limpio de nombre con .strip() para evitar espacios al principio y final evitando que se envíe solo espacios, y verifica si el campo esta vacío y si existe uno igual.
    """
    class Meta:
        model = Categoria
        fields = ['nombre']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()

        if not nombre:
            raise forms.ValidationError("Este campo no puede estar vacío.")

        # Evita el error si estamos editando y el nombre no cambió
        query = Categoria.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)  # Excluye la categoría actual

        if query.exists():
            raise forms.ValidationError("Ya existe una categoría con ese nombre.")

        return nombre