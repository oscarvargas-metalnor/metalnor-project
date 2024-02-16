import os
import django

# Ajusta la siguiente línea para que apunte a la configuración de tu proyecto Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# Importa los modelos Estado y Localidad desde tu aplicación Django
from core.models import Estado, Localidad  # Cambia 'tu_app' por el nombre real de tu aplicación

def migrar_datos_localidades(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Saltamos la línea del encabezado
        next(file)  # Saltamos la línea de separación
        for line in file:
            parts = line.strip().split('|')
            if len(parts) < 3:  # Verificamos que la línea tenga todas las partes necesarias
                continue
            estado_id, nombre_localidad = int(parts[1]), parts[2].strip()
            try:
                estado = Estado.objects.get(id=estado_id)
                Localidad.objects.get_or_create(nombre=nombre_localidad, estado=estado)
            except Estado.DoesNotExist:
                print(f"Estado con ID {estado_id} no encontrado. Localidad '{nombre_localidad}' no fue creada.")

# Especifica la ruta correcta al archivo TXT
file_path = "C:\\Users\\ovargas\\Documents\\proyecto_metalnor\\docs_sistema_gnexus\\areas\\PAISPROVINCIALOCALIDAD_202402141124.txt"

migrar_datos_localidades(file_path)
