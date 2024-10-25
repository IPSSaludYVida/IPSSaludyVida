from django.shortcuts import render
from django.views.generic import ListView

from clinica.models import Usuario


# Create your views here.

class ListaPacientes(ListView):
    model = Usuario
    template_name = 'pacientes/pacientes.html'
    context_object_name = 'pacientes'