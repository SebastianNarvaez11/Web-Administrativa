from django.db import models
from core.validators import *
# Create your models here.


class Materia(models.Model):
    nombre = models.CharField('Nombre', max_length=20, unique=True, validators=[validate_only_letters, MinLengthValidator(4)])
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.nombre



def custom_upload_to(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Docente.objects.filter(pk=instance.pk):
        return 'docentes/' + filename
    else:
        old_instance = Docente.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'docentes/' + filename

class Docente(models.Model):
    nombre = models.CharField('Nombre', max_length=12, validators=[validate_only_letters, MinLengthValidator(2)])
    apellido = models.CharField('Apellido', max_length=12, validators=[validate_only_letters, MinLengthValidator(2)])
    imagen = models.ImageField('Foto', upload_to=custom_upload_to)
    informacion = models.TextField('Información', blank=True, null=True, max_length=150)
    materias = models.ManyToManyField(Materia, verbose_name='Materias que enseña', related_name='obtener_docentes')
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return self.nombre+" "+self.apellido
