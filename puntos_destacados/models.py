from django.db import models

class PuntoDestacado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='puntos/', null=True, blank=True)

    def __str__(self):
        return self.nombre