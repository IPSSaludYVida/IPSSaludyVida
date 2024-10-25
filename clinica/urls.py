from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import *

urlpatterns = [

    path('pacientes', ListaPacientes.as_view(), name='pacientes'),
]