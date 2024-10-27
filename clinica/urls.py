from operator import index

from django.conf.urls.i18n import urlpatterns
from django.urls import path
from.views import *

urlpatterns = [

    path('pacientes', ListaPacientes.as_view(), name='pacientes'),
    #path('', views.index, name='index'),
    path('servicios', ListaServicios.as_view(), name='servicios'),

    path('crear_servicio/', crear_servicio, name='crear_servicio'),

    path('crear_triage/', crear_triage, name='crear_triage'),

    path('eliminar_servicio/<int:id_servicio>/', eliminar_servicio, name='eliminar_servicio'),

    path('editar_servicio/<int:id_servicio>/', editar_servicio, name='editar_servicio'),
    path('', IndexView.as_view(), name='index'),


]