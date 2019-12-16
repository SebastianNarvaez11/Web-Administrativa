from django.forms import ModelForm
from django import forms
from .models import Service


class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = ['titulo', 'descripcion', 'contenido', 'mensualidad',
                  'matricula', 'imagen', 'jornada', 'index', 'estado']