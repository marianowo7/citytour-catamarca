from django.db import models
from usuario.models import Usuario


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


class Recorrido(models.Model):
    nombre = models.CharField(max_length=100, default="recorrido_default")
    descripcion = models.TextField(blank=True, null=True)

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
    unidad = models.ForeignKey('Unidad', on_delete=models.PROTECT)
    puntos_destacados = models.ManyToManyField('PuntoDestacado', blank=True, related_name='recorridos')


    def __str__(self):
        return f"{self.nombre} - {self.get_origen_display()} a {self.get_destino_display()}"
    
    @property
    def cantidad_max_pasajes(self):
        return self.unidad.cantidad_asientos



class Parada(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=200)
    recorrido = models.ForeignKey(Recorrido, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.recorrido}"


class PuntoDestacado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

    
class Itinerario(models.Model):
    recorrido = models.ForeignKey('Recorrido', on_delete=models.PROTECT)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.recorrido.nombre} - {self.recorrido.get_origen_display()} → {self.recorrido.get_destino_display()} | {self.fecha_salida} {self.hora_salida}"


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL,  null=True, blank=True)
    itinerario = models.ForeignKey(Itinerario, on_delete=models.PROTECT, null=True, blank=True)
    metodoPago = models.CharField(max_length=100)

    def __str__(self):
        return f"Reserva de {self.usuario} - {self.recorrido}"
