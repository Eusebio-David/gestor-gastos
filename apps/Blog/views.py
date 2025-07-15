from django.shortcuts import render 
from .models import Post 
from django.core.paginator import Paginator
from django.views.generic import DetailView

# Create your views here.
def PostLista(request):
    """
    Este código te permite mostrar los post divididas en páginas de 6 elementos, para que no se vea una lista muy larga. Además, el usuario puede cambiar de página agregando ?page=2, ?page=3, etc. en la URL.

    obtenemos una lista de posts ordenadas por su id
    luego se divide la lista en paginas que tienen 6 preguntas, lo creamos con Paginator
    en page_number obtenemos el numero de la pagina con request.GET.get('page)
    con el número de pagina que obtuvimos anteriormente se obtiene un objeto de esa página en específico. 
    Por último enviamos los datos por el template
    """
    posts = Post.objects.filter(publicado=True).order_by('-creado')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post/post.html', {'posts': page_obj})

class PostDetalle(DetailView):
    model = Post 
    template_name = 'post/post_detail.html'