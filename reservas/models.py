from django.db import models
from usuario.models import Usuario
from recorrido.models import Recorrido

# Create your models here.

class Reserva (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    recorrido = models.ForeignKey(Recorrido, on_delete=models.PROTECT)
    metodoPago = models.CharField(max_length=100)