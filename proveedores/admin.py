from django.contrib import admin
from .models import Proveedor, TipoProveedor, RubroProveedor, ProveedoresPorSucursal



class ProveedoresPorSucursalInline(admin.TabularInline):
    model = ProveedoresPorSucursal
    extra = 0
    fields = ["proveedor", "sucursal",]
    autocomplete_fields = ["proveedor", "sucursal"]
    ordering = ["sucursal", "proveedor"]
    raw_id_fields = ["proveedor", "sucursal"]


class RubroProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre",)
    ordering = ["nombre"]

admin.site.register(RubroProveedor, RubroProveedorAdmin)


class TipoProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_filter = ("nombre",)
    search_fields = ("nombre",)
    ordering = ["nombre"]

admin.site.register(TipoProveedor, TipoProveedorAdmin)


class ProveedorAdmin(admin.ModelAdmin):
    inlines = (ProveedoresPorSucursalInline,)
    list_display = ("nombre", "cuit", "correo_electronico", "localidad")
    list_filter = ("localidad",)
    search_fields = ("nombre", "cuit", "correo_electronico")
    ordering = ["nombre"]

admin.site.register(Proveedor, ProveedorAdmin)