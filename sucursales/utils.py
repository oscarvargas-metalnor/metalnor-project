from usuarios.models import UsuarioPersonalizado
from .models import Sucursal


def get_sucursales(request):
    sucursales = Sucursal.objects.all()
    if request.user.is_authenticated: #Aqui solo mostramos 1 por ahora hasta que esten todos los roles 
        sucursales = [request.user.sucursal]
    
    return sucursales