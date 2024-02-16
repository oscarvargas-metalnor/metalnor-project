from django.db import models
from django.contrib.auth.models import Group
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import Permission

from simple_history.models import HistoricalRecords

from core.models import AuditMixin
from usuarios.models import UsuarioPersonalizado

from .managers import PuestoManager

# Create your models here.

class TipoSucursal(models.Model):
    nombre = models.CharField(
        max_length=100
    )  # Ejemplos: Central, Sucursal
    
    permite_areas = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.nombre


class Sucursal(AuditMixin):
    TAMAÑOS = (
        ('Micro', 'Micro'),
        ('Chica', 'Chica'),
        ('Mediana', 'Mediana'),
        ('Grande', 'Grande'),
    )
    
    alias = models.CharField(
        max_length=350, 
        verbose_name='Alias',
        help_text='El alias de la sucursal.'
    )
    
    codigo = models.CharField(
        max_length=350, 
        verbose_name='codigo',
        help_text='El código de la sucursal.'
    )
    
    tamaño = models.CharField(
        max_length=350, 
        choices=TAMAÑOS, 
        verbose_name='Tipo',
        help_text='El tipo de sucursal (tamaño).'
    )

    responsable = models.ForeignKey(
        'usuarios.UsuarioPersonalizado',
        on_delete=models.PROTECT,
        verbose_name='Responsable',
        related_name='sucursales',
        help_text='El responsable de la sucursal.'
    )
    
    tipo = models.ForeignKey(
        TipoSucursal,
        on_delete=models.PROTECT,
        verbose_name='Tipo de sucursal',
        related_name='sucursales',
        help_text='El tipo de sucursal.',
        null=True 
    )
    telefonos = GenericRelation(
        "core.Telefono",
    )
    localidad = models.ForeignKey(
        'core.Localidad',
        on_delete=models.PROTECT,
        verbose_name='Localidad',
        related_name='sucursales',
        help_text='La localidad de la sucursal.',
        null=True
    )
        
    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
    
    def __str__(self):
        return "SUC-" + self.codigo + " " + self.alias


class Jerarquia(AuditMixin):
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    
    def __str__(self):
        return self.nombre
    
    
class Area(AuditMixin):
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    sucursal = models.ForeignKey(
        Sucursal, 
        related_name='areas', 
        on_delete=models.PROTECT
    )
    nomenclatura = models.CharField(
        max_length=100,
        verbose_name='Nomenclatura',
        blank=True
    )
    jefe_area = models.ForeignKey(
        'usuarios.UsuarioPersonalizado',
        on_delete=models.PROTECT,
        related_name='jefe_area',
        verbose_name='Jefe de área',
        null=True,
        blank=True,
    )
    gerente_area = models.ForeignKey(
        'usuarios.UsuarioPersonalizado',
        on_delete=models.PROTECT,
        related_name='gerente_area',
        verbose_name='Gerente de área',
        null=True,
        blank=True,
        help_text='El gerente de la área'
    )
    correo_electronico = models.EmailField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.nombre
    

class Puesto(models.Model):
    nombre = models.CharField(
        max_length=100
    )
    descripcion = models.TextField(
        blank=True, 
        null=True
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='puestos',
        verbose_name='Área'
    )
    jerarquia = models.ForeignKey(
        Jerarquia,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='areas',
        verbose_name='Jerarquía',
        help_text='La jerarquía de la área'
    )
    #Permite una estructura organizacional más compleja
    puesto_superior = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='subordinados'
    )

    objects = PuestoManager()
    
    def __str__(self):
        return self.nombre
    
    
#Clase momentanea solo para prueba esta clase pertenece a la aplicacion de empleados o personal
class Empleado(models.Model):
    usuario = models.OneToOneField(UsuarioPersonalizado, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, related_name='empleados', on_delete=models.SET_NULL, null=True, blank=True)
    posicion = models.ForeignKey(Puesto, related_name='empleados', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.usuario.username