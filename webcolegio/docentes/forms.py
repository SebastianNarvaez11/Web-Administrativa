from django.forms import ModelForm
from .models import Materia, Docente


class MateriaForm(ModelForm):

    class Meta:
        model = Materia
        fields = ['nombre']

class DocenteForm(ModelForm):

    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'imagen',
                  'informacion', 'materias']
