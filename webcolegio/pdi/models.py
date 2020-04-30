from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
import re
from core.models import Grado
from docentes.models import Materia
from core.validators import *


# Create your models here.

class Category(models.Model):
    nombre = models.CharField('Nombre', max_length=20, unique=True, validators=[validate_only_letters, MinLengthValidator(4)])
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de modificacion', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-creacion']

    def __str__(self):
        return self.nombre


def custom_upload_to(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Post.objects.filter(pk=instance.pk):
        return 'posts/' + filename
    else:
        old_instance =  Post.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'posts/' + filename
    
    

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=20, unique=True, validators=[validate_only_letters, MinLengthValidator(3)])
    descripcion = models.TextField('Descripcion', max_length=30, blank=True, null=True)
    contenido = RichTextUploadingField('Contenido')
    imagen = models.ImageField('Imagen', upload_to=custom_upload_to) 
    # autor enlazado con los usuarios de django
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category, verbose_name='Categoria', related_name="obtener_posts")
    grado = models.ForeignKey(Grado, verbose_name='Grado', on_delete=models.SET_NULL, blank=True, null=True, related_name="obtener_posts")
    materia = models.ForeignKey(Materia, verbose_name='Materia', on_delete=models.SET_NULL, blank=True, null=True, related_name="obtener_posts")
    slug = models.SlugField('Slug/Url')
    publicacion = models.DateField('Fecha de publicacion', default = now)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de modificacion', auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = re.sub(r'[^a-z0-9+]', '-', self.titulo.lower())
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo
