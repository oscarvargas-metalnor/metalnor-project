from django.urls import path

from . import views

app_name = 'configuraciones_app'

urlpatterns = [
    path('', views.configuraciones, name='configuraciones_index'),
]