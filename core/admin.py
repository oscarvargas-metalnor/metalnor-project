from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import Pais, Estado, Localidad, Telefono, TipoTelefono


# Register your models here.
@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    search_fields = ['app_label', 'model']


class TipoTelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
    ordering = ('nombre',)
    
admin.site.register(TipoTelefono, TipoTelefonoAdmin)

class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero',)
    search_fields = ('id', 'numero',)
    ordering = ('numero',)
    #Content type
    autocomplete_fields = ('content_type', )
    
admin.site.register(Telefono, TelefonoAdmin)
    


class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
    ordering = ('nombre',)
    
admin.site.register(Pais, PaisAdmin)


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais')
    list_filter = ('pais',)
    search_fields = ('id', 'nombre',)
    ordering = ('nombre',)
    
admin.site.register(Estado, EstadoAdmin)


class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'estado')
    list_filter = ('estado',)
    search_fields = ('id', 'nombre',)
    ordering = ('nombre',)
    autocomplete_fields = ('estado',)

admin.site.register(Localidad, LocalidadAdmin)