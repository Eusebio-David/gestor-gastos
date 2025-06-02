from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gasto, Categoria
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from datetime import date 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GastoForm

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
class ListaDeGastos(ListView):
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
    model = Gasto
    template_name = 'gastos/gasto_form.html'
    success_url = reverse_lazy('inicio')

    fields = ['monto', 'categoria', 'descripcion']

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.usuario = self.request.user
            return super().form_valid(form)
        else:
            messages.error(self.request,'Debes inciciar sesión para crear un gasto')
            return redirect('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = date.today().isoformat()
        context['categorias'] = Categoria.objects.all()
        return context
    
    


class DetalleGasto(LoginRequiredMixin, DetailView):
   model = Gasto
 

"""
    esta vista es para editar un gasto, y para ver el detalle del gasto
    se usa la vista CrearGasto para ver y editar gastos, ya que ambas comparten el mismo formulario y el mismo template.
    En el template html el formulario se adapta dependiendo de si es una creación o una edición.
    Si se accede a la vista con un método GET, se muestra el formulario con los datos del gasto.
    si se accede con un método POST, se actualizan los datos del gasto con los datos del formulario.

"""
class GastoEditarDetalle(LoginRequiredMixin, CategoriaContextMixin, View):
    template_name = 'gastos/gasto_detail.html'
    

    #Sobre escribimos la query set para filtrar los gastos del usuario autenticado
    def get_queryset(self):
        return Gasto.objectes.filter(usuario=self.request.user)
    
    
    def get(self, request, pk):
        gasto = get_object_or_404(Gasto,pk=pk) #obtenemos el gasto por su id o pk en este caso
        form = GastoForm(instance=gasto) #lo asignamos al formulario para que se muestre con los datos del gasto
        #obtenemos todas las categorias para mostrarlas en el formulario

        #leer si viene ?ok=true en la url
        ok = request.GET.get('ok')=='true'

        #renderizamos el template con el gasto, el formulario y las categorias en forma de diccionario. 
        return render(request, self.template_name, {
            'gasto':gasto,
            'form': form,
            'ok': ok
        })
    
    def post(self, request, pk):
        gasto = get_object_or_404(Gasto,pk=pk)
        form = GastoForm(request.POST, instance=gasto)

        if form.is_valid():
            form.save()
            return redirect(reverse('gasto_detalle', args=[gasto.pk]) + '?ok=true')


        return render(request, self.template_name,{
            'gasto': gasto,
            'form': form,
            'ok': False
        })
        

class EliminarGasto(LoginRequiredMixin, DeleteView):
    model = Gasto
    success_url = reverse_lazy('inicio')
    def get_queryset(self):
        #Sobreescribimos el método get_queryset para filtrar los gastos del usuario autenticado
        return Gasto.objects.filter(usuario=self.request.user)
      
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'El gasto fue eliminado con éxito.')
        return super().delete(request, *args, **kwargs)


def Inicio(request):
    if request.user.is_authenticated:
        gastos_recientes = Gasto.objects.filter(usuario=request.user)
        return render(request, 'inicio.html', {'gastos': gastos_recientes})
    else:
        return render(request, 'inicio.html')  # sin contexto, o podés pasar otro


    


    