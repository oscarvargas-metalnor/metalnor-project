from django import forms
from django.contrib.auth.forms import UserCreationForm
from sucursales.models import Sucursal
from usuarios.models import UsuarioPersonalizado


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de usuario",
                "class": "form-control form-control-user"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control form-control-user"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de usuario",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Correo",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir contraseña",
                "class": "form-control"
            }
        ))
    sucursal = forms.ModelChoiceField(
        queryset=Sucursal.objects.all(),
        empty_label=None,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'email', 'password1', 'password2', 'sucursal', 'first_name', 'last_name')

    def get_errors_as_dict(self):
        errors_dict = {}
        for field_name, errors in self.errors.items():
            errors_dict[field_name] = errors.as_text()

        return errors_dict