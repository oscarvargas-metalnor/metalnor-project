from django.urls import path
from .views import *

app_name = 'sucursales_app'

urlpatterns = [
    ##################################################################################
    #
    #                             URLS ABM SUCURSALES
    #
    ##################################################################################
    path(
        'lista/', 
        lista_sucursales_view, 
        name='lista_sucursales'
    ),
    path(
        'cambio/', 
        cambio_sucursal_view, 
        name='cambio_sucursal'
    ),
    path(
        'alta/', 
        alta_sucursal_view, 
        name='alta_sucursal'
    ),
    path(
        'baja/',
        baja_sucursal_view,
        name='baja_sucursal'
    ),
    path(
        'modificar/',
        modificar_sucursal_view,
        name='modificar_sucursal'
    ),
    ##################################################################################
    #
    #                             URLS ABM AREAS
    #
    ##################################################################################
    path(
        'areas/lista/',
        lista_areas_view,
        name='lista_areas'
    ),
    path(
        'areas/alta/',
        alta_area_view,
        name='alta_area'
    ),
    path(
        'areas/baja/',
        baja_area_view,
        name='baja_area'
    ),
    path(
        'areas/modificar/',
        modificar_area_view,
    ),
    ##################################################################################
    #
    #                             URLS ABM PUESTOS
    #
    ##################################################################################
    path(
        'puestos/lista/',
        lista_puestos_view,
        name='lista_puestos'
    ),
    path(
        'puestos/alta/',
        alta_puesto_view,
        name='alta_puesto'
    ),
    path(
        'puestos/baja/',
        baja_puesto_view,
        name='baja_puesto'
    ),
    path(
        'puestos/modificar/',
        modificar_puesto_view,
        name='modificar_puesto'
    ),
]
