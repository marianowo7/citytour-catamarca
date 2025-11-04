from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, dni, password=None, **extra_fields):
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, nombre=nombre, dni=dni, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, nombre, dni, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', 'ADMIN')

        return self.create_user(correo, nombre, dni, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('TURISTA', 'Turista'),
        ('OPERADOR', 'Operador'),
    ]

    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    dni = models.PositiveBigIntegerField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='TURISTA')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'dni']

    def __str__(self):
        return self.nombre
