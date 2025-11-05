from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomPasswordResetForm, RegistroForm, LoginForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuario/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(request, username=correo, password=contraseña)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                form.add_error(None, "Correo o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, 'usuario/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'usuario/password_reset.html'
    email_template_name = 'usuario/password_reset_email.txt'  # versión texto
    html_email_template_name = 'usuario/password_reset_email.html'  # versión HTML con estilos
    subject_template_name = 'usuario/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'usuario/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'usuario/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'usuario/password_reset_complete.html'