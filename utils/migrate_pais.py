import os
import django

# Ajusta la siguiente línea para que apunte a la configuración de tu proyecto Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# Importa el modelo Pais desde tu aplicación Django
from core.models import Pais  # Cambia 'tu_app' por el nombre real de tu aplicación

def migrar_datos_paises(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Saltamos la línea del encabezado
        next(file)  # Saltamos la línea de separación
        for line in file:
            nombre_pais = line.strip('| \n')
            if nombre_pais:  # Aseguramos que la línea no esté vacía
                Pais.objects.get_or_create(nombre=nombre_pais)

# Especifica la ruta correcta al archivo TXT
file_path = "C:\\Users\\ovargas\\Documents\\proyecto_metalnor\\docs_sistema_gnexus\\areas\\PAIS_202402141103.txt"

migrar_datos_paises(file_path)
