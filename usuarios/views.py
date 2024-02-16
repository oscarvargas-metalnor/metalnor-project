from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import JsonResponse

from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str



from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import LoginForm, SignUpForm
from .models import UsuarioPersonalizado



def login_view(request):
    # Si el usuario ya está logueado, cerramos la sesión actual
    if request.user.is_authenticated:
        logout(request)
    
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.success(
                    request, 
                    'Usuario o contraseña incorrectos!',
                    extra_tags='warning'
                )
        else:
            messages.success(
                request, 
                'A ocurrido un error!.',
                extra_tags='danger'
            )

    return render(request, "components/login.html", {"form": form})


@login_required(redirect_field_name='login.html')
@user_passes_test(lambda user: user.is_staff)
def register_user_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'Usuario creado exitosamente'
            success = True

            return JsonResponse({'status': 'success', 'message': msg})
        else:
            msg = 'El formulario enviado no es valido'
            print(msg, form.errors)
            return JsonResponse({'status': 'error', 'message': form.get_errors_as_dict()})
    else:
        form = SignUpForm()

    return render(request, "user_create_page.html", {"user_form": form, "msg": msg, "success": success})


def password_recovery_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # Verifica que el email no esté vacío
        if not email:
            messages.error(request, "Por favor, ingrese una dirección de correo electrónico.", extra_tags='danger')
            return redirect(reverse_lazy('usuarios_app:login'))
        
        try:
            user = UsuarioPersonalizado.objects.get(email=email)
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))  # Codificar el ID del usuario
            reset_link = request.build_absolute_uri('/') + f'accounts/reset_password/{uid}/{token}/'
            send_mail(
                'Recuperación de contraseña',
                'Por favor, sigue este enlace para restablecer tu contraseña: ' + reset_link,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(
                request, 
                "Se han enviado instrucciones para restablecer la contraseña a tu correo electrónico.",
                extra_tags='success'
            )
            return redirect(reverse_lazy('usuarios_app:login'))
        except User.DoesNotExist:
            messages.error(
                request, 
                "No se encontró un usuario con ese correo electrónico.",
                extra_tags='danger'
            )
            return redirect(reverse_lazy('usuarios_app:login'))

    return redirect(reverse_lazy('usuarios_app:login'))


def reset_password_view(request, uidb64, token):
    try:
        # Decodificar el ID del usuario y encontrar al usuario
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            token_generator = PasswordResetTokenGenerator()
            if token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                messages.success(
                    request,
                    "Tu contraseña ha sido restablecida.",
                    extra_tags="success"
                )
                return redirect(reverse_lazy('usuarios_app:login'))
            else:
                messages.error(
                    request, 
                    "El enlace para restablecer la contraseña no es válido o ha expirado.",
                    extra_tags="danger"
                )
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        messages.error(request, "Error al restablecer la contraseña.")
    
    return render(request, 'components/reset_password.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('usuarios_app:login'))


def list_user_view(request):
    users = UsuarioPersonalizado.objects.all()
    
    context = {}
    context['users'] = users
    
    return render(request, 'user_list_page.html', context )


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        role = request.POST.get('role')

        user = UsuarioPersonalizado.objects.create_user(username=username, password=password, email=email, role=role)
        user.save()

        return redirect('usuarios_app:user_list')

    return render(request, 'user_create_page.html')