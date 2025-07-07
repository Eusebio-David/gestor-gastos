from .models import Link



def ctx_dict(request):
    """
    Se crea un diccionario llamado ctx, que funciona como variable global
    En una variable links se guardan todos los links creados en la base de datos
    Luego recorremos con un for guardando la key del links con su respectiva url
    """
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx