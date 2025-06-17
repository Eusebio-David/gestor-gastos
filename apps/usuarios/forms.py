# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    """
    Con este metodo hacemos que el campo email no se pueda repetir
    """
    def clean_email(self):
        email = self.cleaned_data.get('email')
        #filtres no da error, devuelve una lista vacia si no hay elementos o un queryset con los elementos que cumplen el filtro
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está en uso.")
        return email