from django.contrib import admin
from .models import Unidad, Recorrido, Parada, PuntoDestacado, Itinerario, Reserva

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('patente', 'cantidad_asientos', 'estado')
    list_filter = ('estado',)
    search_fields = ('patente',)


@admin.register(Recorrido)
class RecorridoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_origen_display', 'get_destino_display', 'unidad')
    list_filter = ('destino', 'unidad')
    search_fields = ('nombre',)
    filter_horizontal = ('puntos_destacados',)


@admin.register(Parada)
class ParadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'recorrido')
    search_fields = ('nombre', 'ubicacion')
    list_filter = ('recorrido',)


@admin.register(PuntoDestacado)
class PuntoDestacadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'ubicacion')
    search_fields = ('nombre', 'descripcion')


@admin.register(Itinerario)
class ItinerarioAdmin(admin.ModelAdmin):
    list_display = ('recorrido', 'fecha_salida', 'hora_salida')
    list_filter = ('fecha_salida', 'recorrido__destino')
    search_fields = ('recorrido__nombre',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'itinerario', 'metodoPago')
    list_filter = ('metodoPago',)
    search_fields = ('usuario__username', 'itinerario__recorrido__nombre')
