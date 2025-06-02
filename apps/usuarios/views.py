from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# accounts/views.py
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm

# accounts/views.py

from django.contrib.auth.models import User


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        
        
        

        current_domian = self.request.get_host()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = f"http://{current_domian}/usuario/activate/{uid}/{token}/"

        # Simulación del correo
        print("🟢 Enlace de activación generado:")
        print(activation_link)

        # En lugar de redirigir, renderizamos la página que muestra el link
        return render(self.request, 'registration/activation_link.html', {
            'activation_link': activation_link,
            
        })
    
    
    def form_invalid(self, form):
    # IMPORTANTE: esto renderiza el template con los errores
        return self.render_to_response(self.get_context_data(form=form))

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Cuenta activada con éxito. Ya podés iniciar sesión.')
            return redirect(reverse_lazy('login'))
        else:
            return render(request, 'registration/activation_invalid.html')

"""
def my_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == 'POST':
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect('index')
        else: 
            print('Error')
    
    return render(request, 'usuarios/login.html')
"""

# Create your views here.
def vista(request):
    return render(request, 'registration/login.html')