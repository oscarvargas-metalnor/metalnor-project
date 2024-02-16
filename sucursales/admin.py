from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from django.db.models import Sum

from .models import Sucursal, Area, Puesto, Empleado, TipoSucursal, Jerarquia



class SucursalAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'alias', 'codigo', 'tamaño', 'responsable', 'telefonos', 'localidad')
    search_fields = ('id', 'alias', 'codigo',)
    list_filter = ('tamaño', 'responsable', 'tipo')
    ordering = ('id', 'alias', 'codigo')
    autocomplete_fields = ('localidad', )
    
    def telefonos(self, obj):
        # Obtiene una lista de números de teléfono como cadenas
        numeros_telefono = [telefono.numero for telefono in obj.telefonos.all()]
        # Une y retorna los números de teléfono con coma
        return ", ".join(numeros_telefono)
  
admin.site.register(Sucursal, SucursalAdmin)


class JerarquiaAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('id', 'nombre',)
    ordering = ('id', 'nombre',)
    
admin.site.register(Jerarquia, JerarquiaAdmin)


class AreaAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'sucursal', 'nomenclatura', 'jefe_area', 'gerente_area')
    search_fields = ('nombre', 'sucursal__alias', 'sucursal__codigo', 'nomenclatura', 'jefe_area__username', 'gerente_area__username')
    list_filter = ('sucursal', 'nomenclatura')
    ordering = ('nombre', 'sucursal__alias', 'sucursal__codigo',)
    autocomplete_fields = ('sucursal',)

admin.site.register(Area, AreaAdmin)


class TipoSucursalAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'permite_areas')
    search_fields = ('nombre', 'permite_areas')
    list_filter = ('nombre',)
    ordering = ('nombre',)

admin.site.register(TipoSucursal, TipoSucursalAdmin)


class PuestoAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'descripcion', 'area', 'get_jefe_area', 'get_gerente_area')
    search_fields = ('nombre', 'descripcion', 'area__nombre', 'area__sucursal__alias', 'area__sucursal__codigo')
    list_filter = ('area',)
    ordering = ('nombre', 'area__nombre', 'area__sucursal__alias', 'area__sucursal__codigo')
    autocomplete_fields = ('area',)

    def get_jefe_area(self, obj):
        return obj.area.jefe_area.username if obj.area.jefe_area else 'N/A'
    get_jefe_area.short_description = 'Jefe de Área'

    def get_gerente_area(self, obj):
        return obj.area.gerente_area.username if obj.area.gerente_area else 'N/A'
    get_gerente_area.short_description = 'Gerente de Área'

admin.site.register(Puesto, PuestoAdmin)