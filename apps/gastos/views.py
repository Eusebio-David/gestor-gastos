from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gasto, Categoria, Presupuesto
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from datetime import date 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GastoForm, PresupuestoForm

"""
Mixin para agregar las categorias al contexto de las vistas que lo hereden.
Este mixin se puede usar en cualquier vista que necesite mostrar las categorias.
"""
class CategoriaContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

# Create your views here.

#vistas para Presupuesto
class CrearPresupuesto(LoginRequiredMixin, CreateView):
    """
    Creamos una vista para crear un presupuesto, o monto el cual va a ser un presupuesto mensual. Partiendo de este monto se irán descontando los gastos. 
    Primero verificamos que no exista ya un presupuesto creado, si existe no podremos crear uno, solo eliminarlo, o modificarlo. 
    Caso contrario podremos crear uno nuevo. 
    """
    model = Presupuesto
    template_name = 'gastos/presupuesto_form.html'
    success_url = reverse_lazy('inicio')
    
    form_class = PresupuestoForm

    def form_valid(self, form):
        usuario = self.request.user
        fecha = form.cleaned_data['fecha_de_expiracion']

        # Verificar si ya existe presupuesto para ese mes/año
        existe = Presupuesto.objects.filter(
            usuario=usuario,
            fecha_de_expiracion__year=fecha.year,
            fecha_de_expiracion__month=fecha.month
        ).exists()

        if existe:
            form.add_error('fecha_de_expiracion', "Ya tienes un presupuesto para ese mes.")
            
            return self.form_invalid(form)

        # Asignar usuario y continuar
        form.instance.usuario = usuario
        messages.success(self.request, "Presupuesto creado con éxito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor revisa los datos ingresado')
        return super().form_invalid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        presupuesto = Presupuesto.objects.filter(usuario=self.request.user).first()
        context['presupuesto'] = presupuesto
        context['today'] = date.today().isoformat()
        return context


class PresupuestoDetalle(LoginRequiredMixin, DetailView):
    """
    Vista enfocada en mostrar el detalle de un presupuesto previamente definito. 
    Mostrara el monto y la fecha la cual es de su expiración.
    """
    model = Presupuesto
    form_class = PresupuestoForm


class PresupuestoEditar(LoginRequiredMixin, UpdateView):
    """
    Vista para poder editar el presupuesto previamente creado. 
    Asiganmos el modelo de presupuesto y el formulario creado en forms.py. 
    Al ser una clase Generica de Django, el funcionamiento lo simplifica facilmente.
    """
    model = Presupuesto
    form_class = PresupuestoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.success(self.request, "Actualizacion del presupuesto con éxito")
        return reverse_lazy('inicio')+'?ok'


class PresupuestoEliminar(DeleteView):

    """
    Vista para poder eliminar un presupuesto previamente definido. Mediante su pk o Primary Key podemos realizar la eliminación. 
    Usamos CBV o clases basadas en vista para simplificar el proceso. 
    """
    model = Presupuesto 
    success_url = reverse_lazy('inicio')
    
    def get_queryset(self):
        #Sobreescribimos el método get_queryset para filtrar los gastos del usuario autenticado
        return Presupuesto.objects.filter(usuario=self.request.user)
    
    #Sobreescrimios el método post para poder enviar un mensaje de éxito cuando se realiza la eliminacíon
    def post(self, request, *args, **kwargs):
        messages.success(request, 'El presupuesto fue eliminado con éxito.')
        return super().post(request, *args, **kwargs)


# vistas para Gastos
class ListaDeGastos(ListView):
    """
    Vista para mostrar una lista de gastos. En caso de que haya gastos creados previamente. 
    """
    model  = Gasto
    template_name = 'gastos/gasto_list.html'
    context_object_name = 'gastos'

    def get_queryset(self):
        return Gasto.objects.filter(usuario = self.request.user)
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now() 
        return context


class CrearGasto(LoginRequiredMixin,CreateView):

    """
    Vista para crear un gasto. Asiganamos el modelo Gasto al modelo de la CBV, cuando se crea exitosamente vuelve a la página de inicio. 
    Verificamos que los datos sean correcto en form_valid y si hay en errores en form_invalid 
    """
    model = Gasto
    form_class = GastoForm
    template_name = 'gastos/gasto_form.html'
    success_url = reverse_lazy('inicio')

   

    def form_valid(self, form):
        #Asignamos el usuario que creo el gasto antes de guardarlo. 
        form.instance.usuario = self.request.user
        messages.success(self.request, "Gasto creado con éxito")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor verifica los datos ingresado del formulario')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = date.today().isoformat()
        context['categorias'] = Categoria.objects.all()
        return context
    



class GastoEditarDetalle(LoginRequiredMixin, CategoriaContextMixin, View):

    """
    esta vista es para editar un gasto, y para ver el detalle del gasto
    se usa la vista CrearGasto para ver y editar gastos, ya que ambas comparten el mismo formulario y el mismo template.
    En el template html el formulario se adapta dependiendo de si es una creación o una edición.
    Si se accede a la vista con un método GET, se muestra el formulario con los datos del gasto.
    si se accede con un método POST, se actualizan los datos del gasto con los datos del formulario.

    Lo hice de esta forma para ver si se puede hacer ambas acciones en un mismo template
    """
    template_name = 'gastos/gasto_detail.html'
    

    #Sobre escribimos la query set para filtrar los gastos del usuario autenticado
    def get_queryset(self):
        return Gasto.objects.filter(usuario=self.request.user)
    
    
    def get(self, request, pk):
        gasto = get_object_or_404(Gasto, pk=pk, usuario=request.user) #obtenemos el gasto por su id o pk en este caso

        form = GastoForm(instance=gasto) #lo asignamos al formulario para que se muestre con los datos del gasto

        #obtenemos todas las categorias para mostrarlas en el formulario
        categorias = Categoria.objects.all()

        #leer si viene ?ok=true en la url
        ok = request.GET.get('ok')=='true'

        #renderizamos el template con el gasto, el formulario y las categorias en forma de diccionario. 
        return render(request, self.template_name, {
            'gasto':gasto,
            'form': form,
            'ok': ok,
            'categorias': categorias
        })
    

    #Sobreescribimos el metodo post par poder enviar los datos y poder actualizar el gasto
    def post(self, request, pk):
        gasto = get_object_or_404(Gasto, pk=pk, usuario=request.user)
        form = GastoForm(request.POST, instance=gasto)
        categorias = Categoria.objects.all()

        if form.is_valid():
            
            gasto_actualizado = form.save(commit=False)
            gasto_actualizado.fecha_creacion = gasto.fecha_creacion  # asegura que no se cambie
            gasto_actualizado.save()
            messages.success(request, "Gasto actualizado correctamente")
            return redirect(reverse('gasto_detalle', args=[gasto.pk]) + '?ok=true')

        return render(request, self.template_name, {
            'gasto': gasto,
            'form': form,
            'ok': False,
            'categorias':categorias
        })
        

class EliminarGasto(LoginRequiredMixin, DeleteView):

    model = Gasto
    success_url = reverse_lazy('inicio')


    def get_queryset(self):
        #Sobreescribimos el método get_queryset para filtrar los gastos del usuario autenticado
        return Gasto.objects.filter(usuario=self.request.user)
      
    def post(self, request, *args, **kwargs):
        messages.success(request, 'El gasto fue eliminado con éxito.')
        return super().post(request, *args, **kwargs)


def Inicio(request):
    if request.user.is_authenticated:
        
        hoy = date.today()
        #mostramos la lista de gastos del usuarioa autenticado, la lista solo va a tener 10 gastos previsualizados, si son más los podrá ver en otro template 
        gastos_recientes = Gasto.objects.filter(usuario=request.user).order_by('-fecha_creacion')[:10]

        #Buscamos si existe un presupuesto
        presupuesto = Presupuesto.objects.filter(
            usuario=request.user,
            fecha_de_expiracion__year=hoy.year,
            fecha_de_expiracion__month=hoy.month
        ).first()

        #verificamos si existe para poder retorna el monto en el inicio, si no existe retornamos $0,0
        if presupuesto:
            return render(request, 'inicio.html', {'gastos': gastos_recientes, 'presupuesto': presupuesto})
        else:
            return render(request, 'inicio.html', {'gastos': gastos_recientes, 'presupuesto': '0,0'})
    else:
        return render(request, 'inicio.html')  # sin contexto, o podemos pasar otro


    


    