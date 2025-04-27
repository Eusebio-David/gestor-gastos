from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Gasto


# Create your views here.
def ExpensesListView(ListView):
    pass

def gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'gastos/index.html',{"gastos":gastos})
