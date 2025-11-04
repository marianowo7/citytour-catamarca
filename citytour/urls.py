from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recorridos/', views.recorridos, name='recorridos'),
    path('reservas/', views.reservas, name='reservas'),
    path('registro_unidad/', views.registrar_unidad, name='registrar_unidad'),
    path('itinerarios/', views.registrar_itinerario, name='registrar_itinerario'),
    path('puntos_destacados/', views.puntos_destacados, name='puntos_destacados'),
    path('puntos_destacados/editar/<int:id>/', views.editar_punto, name='editar_punto'),
    path('puntos_destacados/eliminar/<int:id>/', views.eliminar_punto, name='eliminar_punto'),
]
