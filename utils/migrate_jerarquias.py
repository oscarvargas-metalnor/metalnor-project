import os
import django

# Ajusta la siguiente línea para que apunte a la configuración de tu proyecto Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# Importa el modelo Pais desde tu aplicación Django
from sucursales.models import Jerarquia  # Cambia 'tu_app' por el nombre real de tu aplicación

def migrar_datos_jerarquias(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Saltamos la línea del encabezado
        next(file)  # Saltamos la línea de separación
        for line in file:
            nombre_jerarquia = line.strip('| \n')
            if nombre_jerarquia:  # Aseguramos que la línea no esté vacía
                Jerarquia.objects.get_or_create(nombre=nombre_jerarquia)

# Especifica la ruta correcta al archivo TXT
file_path = "C:\\Users\\ovargas\\Documents\\proyecto_metalnor\\docs_sistema_gnexus\\areas\\JERARQUIAS_202402151110.txt"

migrar_datos_jerarquias(file_path)
