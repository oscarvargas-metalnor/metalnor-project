from django.urls import path, include
from . import views

app_name = 'core_app'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
]
