from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from formtools.wizard.views import SessionWizardView

from core.forms import TelefonoForm, TelefonoFormSet
from core.models import Telefono

from .forms import PersonalForm, EstudiosFormSet, PersonaForm, FamiliarFormSet
from .models import Personal

##################################################################################
#
#                             ABM PERSONAL
#
##################################################################################


class AltaPersonalWizard(SessionWizardView):
    template_name = 'personal/personal_create_page.html'
    form_list = [PersonaForm, PersonalForm, TelefonoFormSet, EstudiosFormSet, FamiliarFormSet]

    def done(self, form_list, **kwargs):
        # Esta función se llama cuando todos los formularios se han validado correctamente
        # Aquí es donde guardas los datos en los modelos correspondientes

        persona_form = form_list[0].save()
        personal = form_list[1].save(commit=False)
        personal.persona = persona_form
        personal.save()

        # Guardar formsets, asumiendo que tienes la instancia para relacionarlos con 'personal'
        telefono_formset = form_list[2]
        for telefono_form in telefono_formset:
            telefono = telefono_form.save(commit=False)
            telefono.personal = personal  # Ajusta según tu modelo y relación
            telefono.save()

        estudios_formset = form_list[3]
        for estudio_form in estudios_formset:
            estudio = estudio_form.save(commit=False)
            estudio.personal = personal  # Ajusta según tu modelo y relación
            estudio.save()

        familiar_formset = form_list[4]
        for familiar_form in familiar_formset:
            familiar = familiar_form.save(commit=False)
            familiar.personal = personal  # Ajusta según tu modelo y relación
            familiar.save()

        # Redireccionar al usuario a una página de éxito o similar
        return HttpResponseRedirect(reverse_lazy('alguna_url_de_exito'))


def baja_personal_view(request, id):
    personal = Personal.objects.get(id=id)
    personal.delete()
    return redirect('sucursales_app:lista_sucursales')


def modificar_personal_view(request, id):
    personal = Personal.objects.get(id=id)
    form = PersonalForm(request.POST or None, instance=personal)

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
    return render(request, 'personal/personal_create_page.html', context)


def lista_sucursales_view(request):
    context = {
        
    }
    
    return render(request, 'personal/sucursal_list_page.html', context)


##################################################################################
#                             FIN ABM PERSONAL
##################################################################################