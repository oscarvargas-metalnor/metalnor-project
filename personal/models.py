from django.db import models
from core.models import AuditMixin
from django.contrib.contenttypes.fields import GenericRelation



class Persona(AuditMixin):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nombre",
        help_text="Escriba el nombre del personal",
    )
    apellido = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Apellido",
        help_text="Escriba el apellido del personal",
    )
    dni = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        verbose_name="DNI",
        help_text="Escriba el DNI del personal sin puntos ni guiones",
    )
    cuil = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="CUIL",
        help_text="Escriba el CUIL del personal sin puntos ni guiones",
    )


class Parentesco(AuditMixin):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nombre del parentesco",
        help_text="Escriba el nombre del parentesco",
    )


class Genero(AuditMixin):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nombre",
        help_text="Escriba el nombre del genero",
    )
    
    def __str__(self):
        return self.nombre.title()


class EstadoCivil(AuditMixin):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nombre",
        help_text="Escriba el nombre del estado civil",
    )
    
    def __str__(self) -> str:
        return self.nombre.title()


class Personal(AuditMixin):

    persona = models.OneToOneField(
        Persona,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Persona",
        related_name="personal",
    )
    
    telefonos = GenericRelation(
        "core.Telefono",
    )
    genero = models.ForeignKey(
        Genero,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Genero",
        help_text="Seleccione el genero del personal",
        related_name="personal",
    )
    codigo_postal = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Codigo postal",
        help_text="Escriba el codigo postal del personal",
    )
    domicilio = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Domicilio",
        help_text="Escriba el domicilio del personal",
    )
    estado_civil = models.ForeignKey(
        EstadoCivil,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Estado civil",
        help_text="Seleccione el estado civil del personal",
        related_name="personal",
    )
    fecha_nacimiento = models.DateField(
        null=False,
        blank=False,
        verbose_name="Fecha de nacimiento",
        help_text="Seleccione la fecha de nacimiento del personal",
    )


class Familiar(AuditMixin):
    persona = models.OneToOneField(
        Persona,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Persona",
        help_text="Identificador de la persona que es el familiar.",
        related_name="como_familiar"
    )
    parentesco = models.ForeignKey(
        Parentesco,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Parentesco",
        help_text="Seleccione el parentesco del familiar respecto al personal.",
        related_name="familiares"
    )
    personal = models.ForeignKey(
        Personal,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Empleado",
        help_text="Empleado al cual está asociado el familiar.",
        related_name="familiares_del_personal"
    )


class EstadoTitulo(AuditMixin):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Estado del titulo",
        help_text="Escriba el nombre del estado del estudio",
    )
    
    def __str__(self) -> str:
        return self.nombre.title()


class TipoEstudio(AuditMixin):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nombre",
        help_text="Escriba el nombre del tipo de estudio",
    )


class Estudios(AuditMixin):
    nombre_titulo = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Titulo",
        help_text="Escriba el nombre que figura en su titulo",
    )
    tipo_estudio = models.ForeignKey(
        TipoEstudio,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Tipo de estudio",
        help_text="Seleccione el tipo de estudio",
        related_name="estudios",
    )
    estado_estudio = models.ForeignKey(
        EstadoTitulo,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Estado del titulo",
        help_text="Seleccione el estado de los estudios",
        related_name="estudios",
    )
    fecha_inicio = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de inicio",
        help_text="Escriba la fecha de inicio del estudio",
        auto_now=False,
        auto_now_add=False,
    )
    fecha_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de fin",
        help_text="Escriba la fecha de fin del estudio",
        auto_now=False,
        auto_now_add=False,
    )
    personal = models.ForeignKey(
        Personal,
        on_delete=models.PROTECT,
        related_name='estudios',
        verbose_name='Personal',
        help_text='Seleccione el personal relacionado con este estudio',
        null=True,
        blank=False,
    )