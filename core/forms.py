from django import forms
from django.forms.models import modelformset_factory
from .models import Telefono
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class TelefonoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TelefonoForm, self).__init__(*args, **kwargs)
        self.fields['numero'].help_text = 'Ingrese el número de teléfono.'
        self.fields['tipo'].help_text = 'Seleccione el tipo de teléfono.'
        # Establecer estilos directamente a través de widgets (opcional)
        self.fields['numero'].widget.attrs.update({'class': 'form-control w-100', 'placeholder': 'Número de teléfono'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-control w-100'})
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('numero', css_class='form-control w-100', placeholder='Número de teléfono'),
            Field('tipo', css_class='form-control w-100', placeholder='Tipo de teléfono'),
        )
    
    class Meta:
        model = Telefono
        fields = ('numero', 'tipo')


TelefonoFormSet = modelformset_factory(Telefono, form=TelefonoForm, extra=1)
