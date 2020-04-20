from django.forms import ModelForm
from .models import Circular



class CircularForm(ModelForm):

    class Meta:
        model = Circular
        fields = ['titulo', 'descripcion', 'contenido','imagen']