from django.db import models

# Create your models here.

class Usuario (models.Model):
    ROLES = [
        {'ADMIN', 'Administrador'},
        {'TURISTA', 'Turista'},
        {'OPERADOR', 'Operador'}
    ]
    
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=150)
    correo = models.EmailField(max_length=254, unique=True)
    dni = models.PositiveBigIntegerField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='TURISTA')

    def __str__(self):
        return self.nombre