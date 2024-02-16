from django.contrib.auth.models import AbstractUser
from django.db import models

from usuarios.managers import UsuarioManager

class UsuarioPersonalizado(AbstractUser):
    
    sucursal = models.ForeignKey('sucursales.Sucursal', on_delete=models.SET_NULL, related_name='usuarios', null=True, blank=True, verbose_name="Sucursal")

    objects = UsuarioManager()
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'custom_user'
    
    def __str__(self):
        return self.first_name + '-' + self.last_name
