from django.urls import path
from .views import *

app_name = 'personal_app'

urlpatterns = [
    path(
        'alta/',
        AltaPersonalWizard.as_view(),
        name='alta_personal'
    )
    
]
