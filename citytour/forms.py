from django import forms
from .models import Recorrido
from .models import Unidad
from .models import Reserva
from .models import Itinerario
from .models import PuntoDestacado

class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = ['recorrido', 'fecha_salida', 'hora_salida', 'observaciones']
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

class RecorridoForm(forms.ModelForm):
    class Meta:
        model = Recorrido
        fields = [
            'nombre',
            'descripcion',
            'origen',
            'destino',
            'fecha_salida',
            'hora_salida',
            'unidad',
            'puntos_destacados',

        ]
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'origen': forms.Select(attrs={'class': 'form-select'}),
            'destino': forms.Select(attrs={'class': 'form-select'}),
            'unidad': forms.Select(attrs={'class': 'form-select'}),
            'puntos_destacados': forms.CheckboxSelectMultiple,
        }

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['patente', 'cantidad_asientos', 'estado']

        
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'itinerario', 'metodoPago']


class PuntoDestacadoForm(forms.ModelForm):
    class Meta:
        model = PuntoDestacado
        fields = ['nombre', 'descripcion', 'ubicacion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }