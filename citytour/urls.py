from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recorridos/', views.recorridos, name='recorridos'),
    path('reservas/', views.reservas, name='reservas'),
    path('registro_unidad/', views.registrar_unidad, name='registrar_unidad'),
    path('unidades/editar/<int:id>/', views.editar_unidad, name='editar_unidad'),
    path('unidades/eliminar/<int:id>/', views.eliminar_unidad, name='eliminar_unidad'),
    path('itinerarios/', views.registrar_itinerario, name='registrar_itinerario'),
    path('puntos_destacados/', views.puntos_destacados, name='puntos_destacados'),
    path('puntos_destacados/editar/<int:id>/', views.editar_punto, name='editar_punto'),
    path('puntos_destacados/eliminar/<int:id>/', views.eliminar_punto, name='eliminar_punto'),
    path('recorridos/editar/<int:id>/', views.editar_recorrido, name='editar_recorrido'),
    path('recorridos/eliminar/<int:id>/', views.eliminar_recorrido, name='eliminar_recorrido'),

]
