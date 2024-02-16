from django.utils import timezone

from sucursales.utils import get_sucursales
from sucursales.models import Sucursal


def set_camp_session(request):
    sucursales = get_sucursales(request)

    try:
        sucursal_id = request.user.sucursal.pk
    except Exception as e:
        print("Exception en set_camp_session: ", str(e))
        if sucursales.count() > 0:
            sucursal_id = sucursales.first().id
        else:
            return None

    # Check if the user has recently logged in
    is_recent_login = request.user.is_authenticated and (
        timezone.now() - request.user.last_login < timezone.timedelta(seconds=2)
    )

    sucursal_actual = request.session.get('sucursal_actual', sucursal_id)

    if is_recent_login:
        sucursal_actual = sucursal_id

    request.session['sucursal_actual'] = sucursal_actual
    sucursal_actual = Sucursal.objects.get(pk=sucursal_actual)
    return sucursal_actual


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def camp_available(user):
    # Your custom test logic goes here
    return user.is_authenticated and user.sucursal.name == "Central" or user.is_staff