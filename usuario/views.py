from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm

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
