from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from .models import Usuario

Usuario = get_user_model()

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'dni', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico')

class CustomPasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        # Buscamos usuarios usando el campo 'correo' en lugar de 'email'
        active_users = Usuario._default_manager.filter(
            is_active=True,
            correo__iexact=email,
        )
        return (u for u in active_users if u.has_usable_password())
