# forms.py

from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, ButtonHolder, Submit, Column, Button

from core.models import Telefono

from .models import Persona, Personal, Estudios, Familiar



class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni', 'cuil']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # Importante para los formsets

        self.helper.layout = Layout(
            Fieldset(
                'Datos Basicos',
                Row(
                    Column('nombre', css_class='form-group col-md-6 mb-0'),
                    Column('apellido', css_class='form-group col-md-6 mb-0'),
                ),
                Row(
                    Column('dni', css_class='form-group col-md-6 mb-0'),
                    Column('cuil', css_class='form-group col-md-6 mb-0'),
                )
            ),
            ButtonHolder(
                Submit('next', 'Siguiente', css_class='button white')
            )
        )


class EstudiosForm(forms.ModelForm):
    class Meta:
        model = Estudios
        fields = ['nombre_titulo', 'tipo_estudio', 'estado_estudio', 'fecha_inicio', 'fecha_fin']

    def __init__(self, *args, **kwargs):
        super(EstudiosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row('nombre_titulo'),
            Row(
                Column('tipo_estudio', css_class='form-group col-md-6 mb-0'),
                Column('estado_estudio', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('fecha_inicio', css_class='form-group col-md-6 mb-0'),
                Column('fecha_fin', css_class='form-group col-md-6 mb-0'),
            )
        )


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['numero', 'tipo']

    def __init__(self, *args, **kwargs):
        super(TelefonoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('numero', css_class='form-group col-md-6 mb-0'),
                Column('tipo', css_class='form-group col-md-6 mb-0'),
            )
        )


class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        exclude = ('personal',)

    def __init__(self, *args, **kwargs):
        super(FamiliarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row('persona'),
            Row('parentesco')
        )


# Formsets
EstudiosFormSet = modelformset_factory(Estudios, form=EstudiosForm, extra=1)
FamiliarFormSet = inlineformset_factory(Personal, Familiar, form=FamiliarForm, extra=1, fk_name='personal')


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ('genero', 'codigo_postal', 'domicilio', 'estado_civil', 'fecha_nacimiento')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # Important for formsets
        self.helper.layout = Layout(
            Fieldset(
                'Datos Basicos',
                Row(
                    Column('genero', css_class='form-group col-md-3 mb-0'),
                    Column('codigo_postal', css_class='form-group col-md-3 mb-0'),
                    Column('estado_civil', css_class='form-group col-md-3 mb-0'),
                    Column('fecha_nacimiento', css_class='form-group col-md-3 mb-0'),
                ),
                Row(
                    Column('domicilio', css_class='form-group col-md-8 mb-0'),
                )
            ),
            ButtonHolder(
                Submit('back', 'Volver', css_class='button white', onclick="window.history.go(-1);"),
                Submit('next', 'Siguiente', css_class='button white')
            )
        )