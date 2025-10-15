from django.db import models

class Unidad(models.Model):

    patente = models.CharField(max_length=10, unique=True)
    cantidad_asientos = models.PositiveIntegerField()

    ESTADOS = [
        ('ACT', 'Activa'),
        ('MAN', 'En Mantenimiento'),
        ('INA', 'Inactiva'),
    ]
    estado = models.CharField(max_length=3, choices=ESTADOS, default='ACT')

    def __str__(self):
        return f"{self.patente} ({self.get_estado_display()})"
