from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'home_temp.html'
    #Mi login personalizado
    login_url = '/usuarios/accounts/login/'
    redirect_field_name = 'redirect_to'
    redirect_authenticated_user = True
    