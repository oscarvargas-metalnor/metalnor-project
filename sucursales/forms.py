from django import forms
from .models import Sucursal, Area, Puesto, Jerarquia

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit




class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['alias', 'codigo', 'tamaño', 'responsable', 'tipo', 'localidad']

    def __init__(self, *args, **kwargs):
        super(SucursalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('alias', css_class='form-group col-md-4 mb-0'),
                Column('codigo', css_class='form-group col-md-2 mb-0'),
                Column('tamaño', css_class='form-group col-md-3 mb-0'),
                Column('tipo', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('localidad', css_class='form-group col-md-6 mb-0'),
                Column('responsable', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )
        

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
        }
        
        
class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
        }
        
        
class JerarquiaForm(forms.ModelForm):
    class Meta:
        model = Jerarquia
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
        }