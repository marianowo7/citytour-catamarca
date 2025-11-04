from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecorridoForm
from .models import Recorrido
from .models import Unidad
from .forms import UnidadForm
from .forms import ItinerarioForm
from .models import Itinerario
from .models import PuntoDestacado
from .forms import PuntoDestacadoForm

@login_required
def editar_punto(request, id):
    punto = get_object_or_404(PuntoDestacado, id=id)
    if request.method == 'POST':
        form = PuntoDestacadoForm(request.POST, instance=punto)
        if form.is_valid():
            form.save()
            return redirect('puntos_destacados')
    else:
        form = PuntoDestacadoForm(instance=punto)
    return render(request, 'citytour/editar_punto.html', {'form': form, 'punto': punto})

@login_required
def eliminar_punto(request, id):
    punto = get_object_or_404(PuntoDestacado, id=id)
    if request.method == 'POST':
        punto.delete()
        return redirect('puntos_destacados')
    return render(request, 'citytour/eliminar_punto.html', {'punto': punto})


@login_required
def puntos_destacados(request):
    puntos = PuntoDestacado.objects.all()
    if request.method == 'POST':
        form = PuntoDestacadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puntos_destacados')
    else:
        form = PuntoDestacadoForm()
    return render(request, 'citytour/puntos_destacados.html', {'form': form, 'puntos': puntos})


@login_required 
def registrar_itinerario(request):
    if request.method == 'POST':
        form = ItinerarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_itinerario')
    else:
        form = ItinerarioForm()

    itinerarios = Itinerario.objects.select_related('recorrido', 'recorrido__unidad').all()
    recorridos = Recorrido.objects.all()

    return render(request, 'citytour/registrar_itinerario.html', {
        'form': form,
        'itinerarios': itinerarios,
        'recorridos': recorridos
    })

@login_required
def inicio(request):
    return render(request, 'citytour/inicio.html')

@login_required
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

@login_required
def reservas(request):
    itinerarios = Itinerario.objects.all()
    return render(request, 'citytour/reservas.html', {'itinerarios': itinerarios})

@login_required
def registrar_unidad(request):
    if request.method == 'POST':
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_unidad')  # Redirige a la misma página o donde prefieras
    else:
        form = UnidadForm()
    
    unidades = Unidad.objects.all()
    return render(request, 'registrar_unidad.html', {'form': form, 'unidades': unidades})

@login_required
def editar_unidad(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    if request.method == 'POST':
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect('registrar_unidad')
    else:
        form = UnidadForm(instance=unidad)
    return render(request, 'citytour/editar_unidad.html', {'form': form, 'unidad': unidad})

@login_required
def eliminar_unidad(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    if request.method == 'POST':
        unidad.delete()
        return redirect('registrar_unidad')
    return render(request, 'citytour/eliminar_unidad.html', {'unidad': unidad})

@login_required
def editar_recorrido(request, id):
    recorrido = get_object_or_404(Recorrido, id=id)
    if request.method == 'POST':
        form = RecorridoForm(request.POST, instance=recorrido)
        if form.is_valid():
            form.save()
            return redirect('recorridos')
    else:
        form = RecorridoForm(instance=recorrido)
    return render(request, 'citytour/editar_recorrido.html', {'form': form, 'recorrido': recorrido})

@login_required
def eliminar_recorrido(request, id):
    recorrido = get_object_or_404(Recorrido, id=id)
    if request.method == 'POST':
        recorrido.delete()
        return redirect('recorridos')
    return render(request, 'citytour/eliminar_recorrido.html', {'recorrido': recorrido})
