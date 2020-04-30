from django.db import models
from docentes.models import Materia
from .validators import *
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Colegio(models.Model):
    nombre = models.CharField('Nombre', max_length=30, validators=[validate_only_letters, MinLengthValidator(7)])
    lema = models.CharField('Lema', max_length=50, validators=[validate_only_letters, MinLengthValidator(7)])
    logo = models.ImageField('Logo', upload_to='colegio', blank=True, null=True)
    email = models.EmailField('Email', max_length=254)
    direccion = models.CharField('Dirección', max_length=30, validators=[MinLengthValidator(7)])
    telefono = models.CharField('Telefono', max_length=12, validators=[validate_only_numbers, MinLengthValidator(5)])
    horarios = models.CharField('Horarios', max_length=100, validators=[MinLengthValidator(2)])
    mision = models.TextField('Misión')
    vision = models.TextField('Vision')
    historia = RichTextUploadingField('Historia')
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    class Meta:
        verbose_name = 'Colegio'
        verbose_name_plural = 'Colegio'

    def __str__(self):
        return self.nombre


def custom_upload_to_grado(instance, filename):
    # primero evalua si existen instancias anteriores de el objeto a crear
    if not Grado.objects.filter(pk=instance.pk):
        return 'grados/' + filename
    else:
        old_instance = Grado.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'grados/' + filename


class Grado(models.Model):
    nombre = models.CharField('Nombre', max_length=15, unique=True, validators=[validate_only_letters, MinLengthValidator(4)])
    jornada = models.CharField('Jornadas', max_length=20, validators=[MinLengthValidator(2)])
    numeracion = models.IntegerField('Numeracion', unique=True, error_messages={"unique":"Ya existe un grado con esta numeracion"})
    materias = models.ManyToManyField(Materia, verbose_name='Asignaturas que ve', related_name='get_materias', blank=True)
    imagen = models.ImageField('Imagen', upload_to=custom_upload_to_grado)
    creacion = models.DateTimeField('Fecha de Creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        ordering = ['numeracion']

    def __str__(self):
        return self.nombre
