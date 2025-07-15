from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import PreguntasFrecuentes
from django.shortcuts import get_list_or_404
from django.core.paginator import Paginator

# Create your views here.



class PreguntasFrecuentesDetalle(DetailView):
    model = PreguntasFrecuentes
    context_object_name= 'pregunta'

def ListaDePreguntas(request):
    """
    Este código te permite mostrar las preguntas frecuentes divididas en páginas de 4 elementos, para que no se vea una lista muy larga. Además, el usuario puede cambiar de página agregando ?page=2, ?page=3, etc. en la URL.

    obtenemos una lista de preguntas ordenadas por su id
    luego se divide la lista en paginas que tienen 4 preguntas, lo creamos con Paginator
    en page_number obtenemos el numero de la pagina con request.GET.get('page)
    con el número de pagina que obtuvimos anteriormente se obtiene un objeto de esa página en específico. 
    Por último enviamos los datos por el template
    """
    lista_preguntas = PreguntasFrecuentes.objects.all().order_by('id')
    paginator = Paginator(lista_preguntas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'preguntas/preguntasFrecuentes_list.html', {'page_obj': page_obj})

