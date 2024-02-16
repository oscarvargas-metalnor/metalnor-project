from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from model_utils.models import TimeStampedModel, SoftDeletableModel
from simple_history.models import HistoricalRecords



class AuditMixin(SoftDeletableModel, TimeStampedModel):
    historial = HistoricalRecords(
        inherit=True
    )
    cambiado_por = models.ForeignKey(
        'usuarios.UsuarioPersonalizado',
        on_delete=models.PROTECT,
        verbose_name='Cambiado por',
        related_name='%(class)s_history',
        null=True,
    )
    is_deleted = models.BooleanField(
        default=False
    )
    
    class Meta:
        abstract = True
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
       
       
class TipoTelefono(models.Model):
    nombre = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.nombre
        
        
class Telefono(models.Model):
    numero = models.CharField(
        max_length=255,
        verbose_name='Número de telefono',
        help_text='Ingrese el número de telefono'
    )
    
    tipo = models.ForeignKey(
        TipoTelefono,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='telefonos',
        verbose_name='Tipo de telefono',
        help_text='Seleccione el tipo de telefono'
    )
    
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.PROTECT
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type', 
        'object_id'
    )

    def __str__(self):
        return self.numero
    

class Pais(AuditMixin):
    nombre = models.CharField(
        max_length=250
    )

    def __str__(self):
        return self.nombre
    

class Estado(AuditMixin):
    nombre = models.CharField(
        max_length=250
    )
    pais = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre
    

class Localidad(AuditMixin):
    nombre = models.CharField(
        max_length=250
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre