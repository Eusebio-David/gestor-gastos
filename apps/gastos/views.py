from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Gasto, Usuario
from django.utils import timezone

# Create your views here.
class GastoListView(ListView):
    model  = Gasto
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now() 
        return context
    

def gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'gastos/index.html',{"gastos":gastos})
