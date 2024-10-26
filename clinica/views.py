from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponse
from django.views.generic import TemplateView



# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Pacientes(TemplateView):
    template_name = 'Paciente.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ServicioPaciente(TemplateView):
    template_name = 'ServicioPaciente.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)






