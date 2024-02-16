import os
import django

# Ajusta la siguiente línea para que apunte a la configuración de tu proyecto Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# Importa los modelos Pais y Estado desde tu aplicación Django
from core.models import Pais, Estado  # Cambia 'tu_app' por el nombre real de tu aplicación

def migrar_datos_provincias(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Saltamos la línea del encabezado
        next(file)  # Saltamos la línea de separación
        for line in file:
            parts = line.strip().split('|')
            if len(parts) < 3:  # Verificamos que la línea tenga todas las partes necesarias
                continue
            pais_id, nombre_provincia = int(parts[1]), parts[2].strip()
            try:
                pais = Pais.objects.get(id=pais_id)
                Estado.objects.get_or_create(nombre=nombre_provincia, pais=pais)
            except Pais.DoesNotExist:
                print(f"Pais con ID {pais_id} no encontrado. Provincia '{nombre_provincia}' no fue creada.")

# Especifica la ruta correcta al archivo TXT
file_path = "C:\\Users\\ovargas\\Documents\\proyecto_metalnor\\docs_sistema_gnexus\\areas\\PAISPROVINCIA_202402141105.txt"

migrar_datos_provincias(file_path)
