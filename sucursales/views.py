from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from .utils import get_sucursales
from .models import Sucursal, Area, Puesto, TipoSucursal, Jerarquia
from .forms import SucursalForm, AreaForm, PuestoForm, JerarquiaForm

from core.models import Telefono
from core.forms import TelefonoFormSet, TelefonoForm



##################################################################################
#
#                             ABM SUCURSALES
#
##################################################################################

def alta_sucursal_view(request):
    TelefonoFormSet = modelformset_factory(Telefono, form=TelefonoForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = SucursalForm(request.POST)
        telefono_formset = TelefonoFormSet(request.POST, queryset=Telefono.objects.none())
        if form.is_valid() and telefono_formset.is_valid():
            sucursal = form.save()
            for telefono_form in telefono_formset:
                telefono = telefono_form.save(commit=False)
                telefono.content_object = sucursal
                telefono.save()
            return redirect('sucursales_app:lista_sucursales')
    else:
        form = SucursalForm()
        telefono_formset = TelefonoFormSet(queryset=Telefono.objects.none())

    return render(request, 'sucursales/sucursal_create_page.html', {'form': form, 'telefono_formset': telefono_formset})


def baja_sucursal_view(request, id):
    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect('sucursales_app:lista_sucursales')


def modificar_sucursal_view(request, id):
    sucursal = Sucursal.objects.get(id=id)
    form = SucursalForm(request.POST or None, instance=sucursal)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('sucursales_app:lista_sucursales')
        else:
            print(form.errors)
            return redirect('sucursales_app:modificar_sucursal', id=id)

    context = {
        'form': form,
    }
    return render(request, 'sucursales/sucursal_create_page.html', context)


def lista_sucursales_view(request):
    context = {
        'sucursales': get_sucursales(request),
    }
    
    return render(request, 'sucursales/sucursal_list_page.html', context)


def cambio_sucursal_view(request):
    if request.POST:
        sucursal_id = request.POST.get('sucursal_id')
        
        if sucursal_id:
            request.session['sucursal_actual'] = int(sucursal_id)
        
        if request.user.is_staff:
            url = reverse_lazy('admin:dashboard')
        else:
            url = reverse_lazy('home')
        
        return redirect(request.META.get('HTTP_REFERER', url))

##################################################################################
#                             FIN ABM SUCURSALES
##################################################################################

##################################################################################
#
#                             ABM AREAS
#
##################################################################################

def alta_area_view(request):
    form = AreaForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('sucursales_app:lista_areas')
        else:
            print(form.errors)
            return redirect('sucursales_app:alta_area')

    context = {
        'form': form,
    }
    return render(request, 'areas/area_create_page.html', context)


def baja_area_view(request, id):
    area = Area.objects.get(id=id)
    area.delete()
    return redirect('sucursales_app:lista_areas')


def modificar_area_view(request, id):
    area = Area.objects.get(id=id)
    form = AreaForm(request.POST or None, instance=area)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('sucursales_app:lista_areas')
        else:
            print(form.errors)
            return redirect('sucursales_app:modificar_area', id=id)

    context = {
        'form': form,
    }
    return render(request, 'areas/area_create_page.html', context)


def lista_areas_view(request):
    context = {
        'areas': Sucursal.objects.all(),
    }

    return render(request, 'areas/area_list_page.html', context)

##################################################################################
#                             FIN ABM SUCURSALES
##################################################################################

##################################################################################
#
#                             ABM PUESTOS
#
##################################################################################

def alta_puesto_view(request):
    form = PuestoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('sucursales_app:lista_puestos')
        else:
            print(form.errors)
            return redirect('sucursales_app:alta_puesto')

    context = {
        'form': form,
    }
    return render(request, 'puestos/puesto_create_page.html', context)

def baja_puesto_view(request, id):
    puesto = Puesto.objects.get(id=id)
    puesto.delete()
    return redirect('sucursales_app:lista_puestos')

def modificar_puesto_view(request, id):
    puesto = Puesto.objects.get(id=id)
    form = PuestoForm(request.POST or None, instance=puesto)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('sucursales_app:lista_puestos')
        else:
            print(form.errors)
            return redirect('sucursales_app:modificar_puesto', id=id)

    context = {
        'form': form,
    }
    return render(request, 'puestos/puesto_create_page.html', context)

def lista_puestos_view(request):
    context = {
        'puestos': Puesto.objects.all(),
    }

    return render(request, 'puestos/puesto_list_page.html', context)

##################################################################################
#                             FIN ABM PUESTOS
##################################################################################

