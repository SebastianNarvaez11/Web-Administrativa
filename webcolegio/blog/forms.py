from django.forms import ModelForm
from .models import Category, Post


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['nombre']


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'contenido',
                  'imagen', 'categoria', 'grado', 'materia']
