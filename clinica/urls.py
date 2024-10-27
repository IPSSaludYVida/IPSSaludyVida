from operator import index

from django.conf.urls.i18n import urlpatterns
from django.urls import path
from.views import IndexView, PacientesIndex, PacientesCrear, ServiciosIndex



urlpatterns = [

    path('pacientes/index', PacientesIndex.as_view(), name='pacientesIndex'),
    path('pacientes/crear', PacientesCrear.as_view(), name='pacientesCrear'),
    path('servicios/index', ServiciosIndex.as_view(), name='serviciosIndex'),
    #path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    #path('Paciente/', view.paciente, name='Paciente'),


]