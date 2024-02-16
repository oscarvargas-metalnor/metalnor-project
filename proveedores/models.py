from django.db import models
from core.models import AuditMixin
from django.contrib.contenttypes.fields import GenericRelation



class RubroProveedor(AuditMixin):
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre",
    )
    descripcion = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )
    
    def __str__(self):
        return self.nombre


class TipoProveedor(AuditMixin):
    nombre = models.CharField(
        max_length=255,
        verbose_name="Nombre",
    )
    descripcion = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )

    def __str__(self):
        return self.nombre


class Proveedor(AuditMixin):
    nombre = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Nombre",
        
    )
    telefonos = GenericRelation(
        "core.Telefono",
    )
    cuit = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="CUIT",
    )
    localidad = models.ForeignKey(
        "core.Localidad",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Localidad",
        related_name="proveedores",
    )
    correo_electronico = models.EmailField(
        max_length=255,
        verbose_name="Correo electrónico",
        blank=True,
    )
    sucursal = models.ManyToManyField(
        "sucursales.Sucursal",
        verbose_name="Sucursales",
        related_name="proveedores",
        through= "proveedores.ProveedoresPorSucursal",
    )
    direccion = models.CharField(
        max_length=350,
        null=True,
        blank=True,
        verbose_name="Dirección",
        help_text="Dirección completa",
    )
    observaciones = models.TextField(
        null=True,
        blank=True,
        verbose_name="Observaciones",
        help_text="Observaciones",
    )
    rubro = models.ForeignKey(
        "proveedores.RubroProveedor",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Rubro",
        related_name="proveedores",
    )
    tipo = models.ForeignKey(
        "proveedores.TipoProveedor",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Tipo",
        related_name="proveedores",
    )
    
    def __str__(self):
        return self.nombre
    
    
class ProveedoresPorSucursal(AuditMixin):
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        verbose_name="Proveedor",
        related_name="proveedores_por_sucursal",
    )
    sucursal = models.ForeignKey(
        "sucursales.Sucursal",
        on_delete=models.PROTECT,
        verbose_name="Sucursal",
        related_name="proveedores_por_sucursal",
    )
    