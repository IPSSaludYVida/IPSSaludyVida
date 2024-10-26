from operator import index

from django.conf.urls.i18n import urlpatterns
from django.urls import path
from.views import IndexView


urlpatterns = [
    path('pacientes', ListaPacientes.as_view(), name='pacientes'),
    #path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('Paciente/', view.paciente, name='Paciente'),


]