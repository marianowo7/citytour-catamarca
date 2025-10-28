from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recorridos/', views.recorridos, name='recorridos'),
    path('reservas/', views.reservas, name='reservas'),
]
