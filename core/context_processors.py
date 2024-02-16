from django.urls import reverse

from core.utils import set_camp_session
from sucursales.utils import get_sucursales
from .sidebar_options import common_menus, group_specific_menus



def sucursales(request):
    # Obtén las sucursales disponibles y devuélvelas en el contexto
    return {
        'sucursales': get_sucursales(request),
        'camp_selected': set_camp_session(request) or "Sucursal sin asociar"
    }

# Función para generar los elementos del menú basado en los grupos del usuario
def sidebar(request):
    sidebar_items = []

    # Primero, añade las opciones de menú comunes
    sidebar_items.extend(common_menus)

    # Luego, verifica las opciones específicas de los grupos y las añade si corresponde
    user_groups = request.user.groups.values_list('name', flat=True)  # Obtener los nombres de los grupos del usuario
    for config in group_specific_menus:
        # Verificar si el usuario pertenece a alguno de los grupos especificados en la configuración
        if any(group in user_groups for group in config["groups"]):
            sidebar_items.extend(config["menus"])  # Añadir las opciones de menú específicas de los grupos

    return {"sidebar_items": sidebar_items}