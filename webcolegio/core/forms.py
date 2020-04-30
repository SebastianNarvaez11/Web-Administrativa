from django.forms import ModelForm
from django import forms
from .models import Colegio, Grado
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ColegioForm(ModelForm):
    class Meta:
            model = Colegio
            fields = ['nombre', 'lema', 'logo',
                      'email', 'direccion', 'telefono',
                      'horarios', 'mision', 'vision',
                      'historia']


class GradoForm(ModelForm):
    class Meta:
        model = Grado
        fields = ['nombre', 'numeracion', 'jornada', 'imagen', 'materias']
