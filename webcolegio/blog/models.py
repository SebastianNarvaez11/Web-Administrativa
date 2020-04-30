from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

def custom_upload_to(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Circular.objects.filter(pk=instance.pk):
        return 'posts/' + filename
    else:
        old_instance =  Circular.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'posts/' + filename


class Circular(models.Model):
    titulo = models.CharField('Titulo', max_length=200, unique=True)
    descripcion = models.TextField('Descripcion', max_length=300, blank=True, null=True)
    contenido = RichTextField('Contenido')
    imagen = models.ImageField('Imagen', upload_to=custom_upload_to) 
    # autor enlazado con los autores de django
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de modificacion', auto_now=True)
    hora = models.DateTimeField('Hora creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Circular'
        verbose_name_plural = 'Circulares'
        ordering = ['-hora']

    def __str__(self):
        return self.titulo