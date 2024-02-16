from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from project import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('compras/', include('compras.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('personal/', include('personal.urls')),
    path('sucursales/', include('sucursales.urls')),
    path('usuarios/', include("usuarios.urls")),
    path('ventas/', include('ventas.urls')),
    path('configuraciones/', include('configuraciones.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
