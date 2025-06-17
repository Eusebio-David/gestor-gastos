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

# importaciones para restablecimiento de contraseña
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.models import User


class SignUpView(CreateView):
    """
    Vista para poder crear un usuario.
    Utilizamos el CustomUserCreationForm definido de Django para poder utilizar los datos y verificar su validez. 
    Una vez creado, y ver que todo es válido, nos da un link que en un futuro deberia ser enviado por correo con un link de activación. 
    """
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        """
        Procesa un formulario de registro de usuario cuando es válido.

        Este método se ejecuta cuando el formulario de creación de usuario es válido. Realiza lo siguiente:
        1. Guarda temporalmente el usuario sin activarlo (`is_active=False`) para requerir activación por correo.
        2. Genera un enlace de activación único utilizando el `uid` codificado y un token seguro.
        3. Muestra por consola (modo prueba) el enlace generado para activación de cuenta.
        4. Renderiza una plantilla que contiene el enlace de activación, en lugar de redirigir automáticamente.

        Args:
            form (UserCreationForm): El formulario de registro ya validado.

        Returns:
            HttpResponse: Renderiza la plantilla `activation_link.html` con el enlace de activación incluido.
        """
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        
        
        

        current_domian = self.request.get_host()#obtiene el dominio actual ya que estamos en modo desarrollo

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

    """
    Vista encargada de activar una cuenta de usuario a través de un enlace enviado por correo electrónico.

    Este enlace incluye un UID codificado y un token de seguridad. Al acceder al enlace:

    - Se decodifica el UID para obtener el ID del usuario.
    - Se valida el token con el usuario correspondiente.
    - Si todo es válido, se activa la cuenta (cambiando `is_active` a True).
    - Se muestra un mensaje de éxito y se redirige al login.
    - Si la validación falla, se muestra una plantilla de error de activación.

    Parámetros:
        uidb64 (str): ID del usuario codificado en base64.
        token (str): Token de activación generado con `default_token_generator`.

    Redirecciona:
        - A la página de login si la activación fue exitosa.
        - A una página de error (`activation_invalid.html`) si el token es inválido o el usuario no existe.
    """

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


class ReenviarPasswordResetEmailView(View):
    """
    Vista encargada de reenviar el correo de restablecimiento de contraseña utilizando la dirección
    de correo almacenada previamente en la sesión del usuario.

    Esta vista se utiliza cuando, tras un intento de recuperación de contraseña, el usuario desea reenviar
    el correo sin tener que volver a introducir su email.

    Funcionamiento:
    - Obtiene el email almacenado en la sesión bajo la clave 'reset_email'.
    - Si existe, crea un formulario de reseteo con ese email y lo valida.
    - Si es válido, se vuelve a enviar el correo de recuperación utilizando las plantillas correspondientes.
    - Se muestran mensajes de éxito o error según el caso, y se redirige al flujo adecuado.

    Redirecciones:
    - A 'password_reset_done' si el correo se reenvía correctamente.
    - A 'password_reset' si no hay un correo en sesión o si el formulario no es válido.
    """

    def post(self, request, *args, **kwargs):
        email = request.session.get('reset_email')

        if email:
            form = PasswordResetForm({'email': email})

            if form.is_valid():
                form.save(
                    request=request,
                    use_https=request.is_secure(),
                    subject_template_name='registration/password_reset_subject.txt',
                    email_template_name='registration/password_reset_email.html',
                )
                messages.success(request, 'Se ha reenviado el correo de restablecimiento.')
                return redirect('password_reset_done')
            else:
                messages.error(request, 'El formulario no es válido.')
                return redirect('password_reset')

        messages.error(request, 'No se encontró un correo electrónico en la sesión.')
        return redirect('password_reset')

class MiPasswordResetView(PasswordResetView):
    """
    Vista personalizada para el formulario de restablecimiento de contraseña.

    Esta vista extiende el comportamiento estándar de `PasswordResetView` para almacenar 
    el correo electrónico ingresado por el usuario en la sesión (`request.session`). 
    Esto permite reutilizar el email más adelante, por ejemplo, para reenviar el correo 
    de restablecimiento sin necesidad de volver a ingresarlo manualmente.

    Funcionamiento:
    - Cuando el formulario es válido, se extrae el email desde `form.cleaned_data`.
    - Se guarda el email en la sesión bajo la clave `'reset_email'`.
    - Luego se continúa con el comportamiento original de la vista padre.

    Clave de sesión utilizada:
    - 'reset_email': almacena el email ingresado por el usuario en el formulario.
    """
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        self.request.session['reset_email'] = email
        return super().form_valid(form)