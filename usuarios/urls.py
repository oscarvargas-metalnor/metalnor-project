from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'usuarios_app'

urlpatterns = [
    path(
        'accounts/login/',
        login_view, 
        name='login'
    ),
    path(
        'accounts/register/',
        register_user_view, 
        name='register'
    ),
    path(
        'accounts/logout/', 
        logout_view, 
        name='logout'
    ),

    # DJANGO RESET PASSWORD -> PARA CAMBIO DE PASSWORD OLVIDADA
    path(
        'accounts/recovery-password/',
        password_recovery_view,
        name='recovery_password'
    ),
    path(
        'accounts/reset_password/<uidb64>/<token>/', 
        reset_password_view, 
        name='reset_password'
    ),
    
    # Rutas para administrar el personal de la empresa
    path(
        'users/create/',
        create_user_view,
        name='user_create'
    ),
    path(
        'users/list/',
        list_user_view,
        name='user_list'
    ),
]