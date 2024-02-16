from django.contrib import admin
from .models import Persona, Parentesco, Genero, EstadoCivil, EstadoTitulo, TipoEstudio, Estudios, Personal, Familiar

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'cuil')
    search_fields = ('nombre', 'apellido', 'dni')

@admin.register(Parentesco)
class ParentescoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(EstadoTitulo)
class EstadoTituloAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(TipoEstudio)
class TipoEstudioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class EstudiosInline(admin.TabularInline):
    model = Estudios
    extra = 1

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('get_nombre', 'get_apellido', 'genero', 'codigo_postal', 'domicilio', 'estado_civil', 'fecha_nacimiento')
    search_fields = ('persona__nombre', 'persona__apellido')
    inlines = [EstudiosInline]

    def get_nombre(self, obj):
        return obj.persona.nombre
    get_nombre.admin_order_field = 'persona__nombre'  # Permite ordenar por este campo en el admin
    get_nombre.short_description = 'Nombre'

    def get_apellido(self, obj):
        return obj.persona.apellido
    get_apellido.admin_order_field = 'persona__apellido'
    get_apellido.short_description = 'Apellido'

class FamiliarInline(admin.TabularInline):
    model = Familiar
    fk_name = 'personal'
    extra = 1

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('get_nombre', 'get_apellido', 'parentesco', 'get_empleado_nombre')
    search_fields = ('persona__nombre', 'persona__apellido', 'personal__persona__nombre')

    def get_nombre(self, obj):
        return obj.persona.nombre
    get_nombre.short_description = 'Nombre del Familiar'

    def get_apellido(self, obj):
        return obj.persona.apellido
    get_apellido.short_description = 'Apellido del Familiar'

    def get_empleado_nombre(self, obj):
        return obj.personal.persona.nombre + " " + obj.personal.persona.apellido
    get_empleado_nombre.short_description = 'Empleado Asociado'
