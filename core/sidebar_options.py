from django.urls import reverse

# Opciones de menú comunes a muchos grupos
common_menus = [
    # Puedes añadir opciones de menú comunes a todos los grupos aquí
]

# Configuraciones específicas de menú por grupo
group_specific_menus = [
    {
        "groups": ["Jefe de Desarrollo Informatico"],
        "menus": [
            {
                "title": "Administrar personal",
                "icon": "mdi mdi-account-circle",
                "sub_items": [
                    {
                        "title": "Ver Personal", 
                        "icon": "mdi mdi-account-search"
                    },
                    {
                        "title": "Nuevo Personal", 
                        "icon": "mdi mdi-account-plus",
                        "url": reverse('personal_app:alta_personal')
                    },
                ],  
            },
            {
                'title': 'Hallazgos',
                'icon': 'mdi mdi-magnify',
            },
            {
                'title': 'Sucursales',
                'icon': 'mdi mdi-store',
            },
            {
                'title': 'Alquileres',
                'icon': 'mdi mdi-home',
            },
            {
                'title': 'Contable',
                'icon': 'mdi mdi-calculator',
            },
            {
                'title': 'Parámetros y Estadísticas',
                'icon': 'mdi mdi-chart-line',
            },
            {
                'title': 'Stock',
                'icon': 'mdi mdi-package-variant-closed',
            },
            {
                'title': 'Caja',
                'icon': 'mdi mdi-cash-multiple',
            },
            {
                'title': 'Compras',
                'icon': 'mdi mdi-cart',
            },
            {
                'title': 'Ventas',
                'icon': 'mdi mdi-currency-usd',
            },
            {
                'title': 'Metalnor',
                'icon': 'mdi mdi-factory',
            },
            {
                'title': 'Cargas',
                'icon': 'mdi mdi-truck',
            },
            {
                'title': 'Bascula',
                'icon': 'mdi mdi-scale',
            },
            {
                'title': 'Guardia',
                'icon': 'mdi mdi-shield',
            },
            {
                'title': 'Servicio de fletes',
                'icon': 'mdi mdi-road-variant',
            },
            {
                'title': 'Administracion sistema',
                'icon': 'mdi mdi-settings',
                'url': reverse('configuraciones_app:configuraciones_index')
            }
        ],
    },
    {
        "groups": ["OtroGrupoEspecifico"],
        "menus": [
            # Opciones de menú específicas para OtroGrupoEspecifico
        ],
    },
    # Añadir configuraciones adicionales para otros grupos específicos aquí
]