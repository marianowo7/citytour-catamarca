from django.shortcuts import render, redirect
from .forms import RecorridoForm
from .models import Recorrido

# Create your views here.

def inicio(request):
    return render(request, 'citytour/inicio.html')

def recorridos(request):
    if request.method == 'POST':
        form = RecorridoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recorridos')  # recarga la misma página
    else:
        form = RecorridoForm()

    recorridos = form.Meta.model.objects.all()
    return render(request, 'citytour/recorridos.html', {'form': form, 'recorridos': recorridos})

def reservas(request):
    return render(request, 'citytour/reservas.html')