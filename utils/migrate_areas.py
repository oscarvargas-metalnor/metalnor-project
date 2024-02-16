import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # Ajusta a tu configuración de Django
django.setup()

from sucursales.models import Area, Sucursal  # Asegúrate de que los modelos estén correctamente importados

def migrar_datos_areas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Saltamos la línea del encabezado
        next(file)  # Saltamos la línea de separación
        for line in file:
            parts = [part.strip() for part in line.split('|') if part.strip()]
            if len(parts) != 3:
                continue
            
            nombre, estado, nomenclatura = parts
            estado = 'Activo' if estado == 'A' else 'Baja'
            sucursal = Sucursal.objects.filter(alias="CENTRAL").first()  # Este es solo un ejemplo, ajusta según tu lógica
            
            Area.objects.create(
                nombre=nombre,
                sucursal=sucursal,
                estado=estado,
                nomenclatura=nomenclatura
            )

# Asegúrate de ajustar la ruta al archivo TXT según tu estructura de archivos
file_path = "C:\\Users\\ovargas\\Documents\\proyecto_metalnor\\docs_sistema_gnexus\\areas\\AREAS_202402140952.txt"

migrar_datos_areas(file_path)
