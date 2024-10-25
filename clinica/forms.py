from django import forms
from .models import Usuario, Servicio
from datetime import datetime


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['tipo_documento','numero_documento','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','fecha_nacimiento',
                  'hora_nacimiento','sexo_biologico','ident_genero','ocupacion','donacion','voluntad','nacionalidad','pais_residencia',
                  'departamento_municipio','comunidad_etnia', 'etnia','zona_residencia','entidad']

        labels = {
            'tipo_documento':'Tipo de documento',
            'numero_documento':'Numero de documento',
            'primer_nombre':'Primer nombre',
            'segundo_nombre':'Segundo nombre',
            'primer_apellido':'Primer apellido',
            'segundo_apellido':'Segundo apellido',
            'fecha_nacimiento':'Fecha nacimiento',
            'hora_nacimiento':'Hora nacimiento',
            'sexo_biologico':'Sexo de bilogico',
            'ident_genero':'Identificador genero',
            'ocupacion' : 'ocupacion',
            'donacion' : '¿Oposición a donación?',
            'voluntad' : 'Documento de voluntad anticipada',
            'nacionalidad' : 'nacionalidad',
            'pais_residencia' : 'pais de residencia',
            'departamento_municipio':'departamento y municipio',
            'comunidad_etnia':'comunidad etnica',
            'etnia' : 'etnia',
            'zona_residencia' : 'zona de residencia',
            'entidad' : 'entidad de salud',

        }
        widgets = {
            'tipo_documento': forms.Select(
                attrs= {
                    'class': 'form-control',
                }
            ),

            'numero_documento': forms.TextInput(
                attrs= {
                    'id':'identificacion',
                    'class': 'form-control',
                    'placeholder':'Ingrese el numero de documento',
                    'longitudmin':'3',
                    'longitudmax':'20',
                    'titulo':'Solo se permiten numeros'

                }
            ),
            'primer_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el primer nombre',
                    'longitudmin':'2',
                    'longitudmax':'60',
                    'titulo':'Solo se permiten letras'
                }
            ),
            'segundo_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el segundo nombre',
                    'longitudmin':'2',
                    'longitudmax':'60',
                    'titulo':'Solo se permiten letras'
                }
            ),
            'primer_apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el primer apellido',
                    'longitudmin':'2',
                    'longitudmax':'60',
                    'titulo':'Solo se permiten letras'
                }
            ),
            'segundo_apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el segundo apellido',
                    'longitudmin':'2',
                    'longitudmax':'60',
                    'titulo':'Solo se permiten letras'
                }
            ),

            'fecha_nacimiento': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'tipo': 'date-local',
                    'maximo': datetime.now().strftime('%d/%m/%Y'),

                }
            ),

            'hora_nacimiento': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'tipo': 'time-local',
                    'maximo': datetime.now().strftime('%H:%M'),
                }
            ),

            'sexo_biologico': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'ident_genero': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'ocupacion': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'donacion': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'voluntad': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'nacionalidad': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'pais_residencia': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'departamento_municipio': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comunidad_etnia': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'etnia': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'zona_residencia': forms.Select(attrs={
                'class': 'form-control',
                }
            ),
            'entidad': forms.Select(attrs={
                'class': 'form-control',
                }
            )
        }