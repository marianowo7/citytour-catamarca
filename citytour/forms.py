from django import forms
from .models import Recorrido

class RecorridoForm(forms.ModelForm):
    class Meta:
        model = Recorrido
        fields = ['origen', 'destino', 'fecha_salida', 'hora_salida', 'unidad']
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'origen': forms.Select(attrs={'class': 'form-select'}),
            'destino': forms.Select(attrs={'class': 'form-select'}),
            'unidad': forms.Select(attrs={'class': 'form-select'}),
        }
