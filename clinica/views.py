from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse
from django.views.generic import TemplateView


from django.views.generic import ListView

from clinica.models import Usuario


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class PacientesIndex(TemplateView):
    template_name = 'pacientes/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class PacientesCrear(TemplateView):
    template_name = 'pacientes/crear.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ServiciosIndex(TemplateView):
    template_name = 'servicios/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)







'''class ListaPacientes(ListView):
    model = Usuario
    template_name = 'pacientes/pacientes.html'
    context_object_name = 'pacientes'''