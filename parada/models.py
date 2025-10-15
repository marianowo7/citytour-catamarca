from django.db import models
from recorridos.models import Recorrido


# Create your models here.
class Parada (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=200)
    recorrido = models.ForeignKey(Recorrido, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.recorrido.nombre}"