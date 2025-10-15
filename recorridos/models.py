from django.db import models

from unidades.models import Unidad

class Recorrido(models.Model):
    ORIGENES = [
        ('TER', 'Estación Terminal'),
    ]

    DESTINOS = [
        ('BAL', 'Balcozna'),
        ('ROD', 'El Rodeo'),
        ('GRU', 'La Gruta'),
    ]

    origen = models.CharField(max_length=3, choices=ORIGENES, default='TER')
    destino = models.CharField(max_length=3, choices=DESTINOS)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.get_origen_display()} a {self.get_destino_display()} | {self.fecha_salida} {self.hora_salida}"


    @property
    def cantidad_max_pasajes(self):
        return self.unidad.cantidad_asientos
