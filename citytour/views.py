from django.contrib.auth.decorators import login_required
from usuario.decorators import role_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecorridoForm
from .models import Recorrido
from .models import Unidad
from .forms import UnidadForm
from .forms import ItinerarioForm
from .models import Itinerario
from .models import PuntoDestacado
from .forms import PuntoDestacadoForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Recorrido, Reserva
from django.db import models
from django.contrib import messages
from django.db.models import Sum
from .models import Itinerario, Reserva
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Itinerario, Reserva


@login_required
@role_required(['ADMIN'])
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
@role_required(['ADMIN'])
def eliminar_punto(request, id):
    punto = get_object_or_404(PuntoDestacado, id=id)
    if request.method == 'POST':
        punto.delete()
        return redirect('puntos_destacados')
    return render(request, 'citytour/eliminar_punto.html', {'punto': punto})


@login_required
@role_required(['ADMIN'])
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
@role_required(['ADMIN'])
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

def inicio(request):
    return render(request, 'citytour/inicio.html')

@login_required
@role_required(['ADMIN'])
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

    if request.user.rol == "TURISTA":
        reservas = Reserva.objects.filter(usuario=request.user)
    else:
        reservas = Reserva.objects.all()

    if request.method == "POST":
        itinerario_id = request.POST.get("itinerario")
        cantidad_pasajeros = request.POST.get("cantidad_pasajeros")

        if itinerario_id and cantidad_pasajeros:
            itinerario = Itinerario.objects.get(id=itinerario_id)
            cantidad_pasajeros = int(cantidad_pasajeros)

            reservados = (
                Reserva.objects.filter(itinerario=itinerario)
                .aggregate(total=Sum("cantidad_pasajeros"))
                .get("total")
                or 0
            )
            capacidad_total = itinerario.recorrido.unidad.cantidad_asientos
            disponibles = capacidad_total - reservados

            if cantidad_pasajeros <= disponibles:
                Reserva.objects.create(
                    usuario=request.user,
                    itinerario=itinerario,
                    cantidad_pasajeros=cantidad_pasajeros,
                    metodoPago="No especificado",  
                    fecha_reserva=timezone.now(),
                )
            else:
                print("No hay suficientes asientos disponibles")

        return redirect("reservas")

    itinerarios_info = []
    for i in itinerarios:
        reservados = (
            Reserva.objects.filter(itinerario=i)
            .aggregate(total=Sum("cantidad_pasajeros"))
            .get("total")
            or 0
        )
        capacidad_total = i.recorrido.unidad.cantidad_asientos
        disponibles = capacidad_total - reservados
        puntos = i.recorrido.puntos_destacados.all()

        itinerarios_info.append({
            "id": i.id,
            "recorrido": i.recorrido,
            "fecha_salida": i.fecha_salida,
            "hora_salida": i.hora_salida,
            "capacidad_total": capacidad_total,
            "reservados": reservados,
            "disponibles": disponibles,
            "puntos": puntos,
        })

    context = {
        "itinerarios": itinerarios,
        "reservas": reservas,
        "itinerarios_info": itinerarios_info,
    }

    return render(request, "citytour/reservas.html", context)


@login_required
@role_required(['ADMIN'])
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
@role_required(['ADMIN'])
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
@role_required(['ADMIN'])
def eliminar_unidad(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    if request.method == 'POST':
        unidad.delete()
        return redirect('registrar_unidad')
    return render(request, 'citytour/eliminar_unidad.html', {'unidad': unidad})

@login_required
@role_required(['ADMIN'])
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
@role_required(['ADMIN'])
def eliminar_recorrido(request, id):
    recorrido = get_object_or_404(Recorrido, id=id)
    if request.method == 'POST':
        recorrido.delete()
        return redirect('recorridos')
    return render(request, 'citytour/eliminar_recorrido.html', {'recorrido': recorrido})


def informes(request):
    return render(request, 'citytour/informes.html')

def informe_recorridos_activos(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recorridos_activos.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 800, "Informe de Recorridos Activos")

    recorridos = Recorrido.objects.all()
    y = 760
    for r in recorridos:
        texto = f"{r.nombre} - {r.get_origen_display()} → {r.get_destino_display()} - Unidad: {r.unidad.patente}"
        p.drawString(50, y, texto)
        y -= 20

    p.showPage()
    p.save()
    return response


def informe_reservas_por_recorrido(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reservas_por_recorrido.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(180, 800, "Informe de Reservas por Recorrido")

    reservas = Reserva.objects.select_related('itinerario__recorrido')
    y = 760
    for r in reservas:
        texto = f"Recorrido: {r.itinerario.recorrido.nombre} - Pasajero: {r.usuario.nombre} ({r.usuario.dni})"
        p.drawString(50, y, texto)
        y -= 20

    p.showPage()
    p.save()
    return response


def informe_pasajeros_por_viaje(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pasajeros_por_viaje.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(180, 800, "Estadísticas de Pasajeros por Viaje")

    itinerarios = Reserva.objects.values('itinerario__recorrido__nombre').annotate(total=models.Count('id'))
    y = 760
    for i in itinerarios:
        texto = f"{i['itinerario__recorrido__nombre']}: {i['total']} pasajeros"
        p.drawString(50, y, texto)
        y -= 20

    p.showPage()
    p.save()
    return response