from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage 
from .forms import ContactoForm 
from .models import InformacionContacto

# Create your views here.

def Contacto(request):
    
    contacto_form = ContactoForm()
    if request.method == 'POST':
        contacto_form = ContactoForm(data=request.POST)
        if contacto_form.is_valid():
            nombre = request.POST.get('nombre','')
            apellido = request.POST.get('apellido','')
            email = request.POST.get('email', '')
            contenido = request.POST.get('contenido','')
            asunto = request.POST.get('subject')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Asunto {}".format(asunto),
                "Getor de Gastos: Nuevo mensaje de contacto",
                "De {}{} <{}>\n\nEscribió: \n\n{}".format(nombre, apellido, email, contenido),
                "no-contestar@inbox.mailtrap.io",
                ["davideusebio033@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                print('se envio')
                return redirect(reverse('contacto')+"?ok=1")
            except Exception as e:
                # Algo no fue bien 
                print("error al enviar corre: {e}")
                return redirect(reverse('contacto')+"?fail=1")
           
    informacion = InformacionContacto.objects.first()
    print(informacion)
    infoContacto =  informacion

    if not infoContacto:
        infoContacto = 'información no encontrada'
    
        
           
   
    return render(request, 'contacto/contacto.html',{'form':contacto_form, 'informacion':infoContacto})
   

   
    
