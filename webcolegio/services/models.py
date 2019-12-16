from django.db import models
import re
from ckeditor.fields import RichTextField
# Create your models here.

def custom_upload_to(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Service.objects.filter(pk=instance.pk):
        return 'services/' + filename
    else:
        old_instance =  Service.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'services/' + filename
    

class Service(models.Model):
    titulo = models.CharField('Titulo', max_length=20, blank=False, null=False, unique=True)
    slug = models.SlugField('Slug/Url')
    descripcion = models.CharField('Descripción', max_length=50, blank=False, null=False  )
    contenido = RichTextField('Contenido')
    mensualidad = models.IntegerField('Mensualidad')
    matricula = models.IntegerField('Matricula')
    imagen = models.ImageField('Imagen', upload_to=custom_upload_to)
    jornada = models.CharField('Jornada(s)', max_length=80, blank=True, null=True)
    index = models.BooleanField('Mostrar en el inicio', default=True)
    estado = models.BooleanField('Publicado/Oculto', default=True)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    def save(self, *args, **kwargs):#genera el slug desde el titulo - importar re
        self.slug = re.sub(r'[^a-z0-9+]', '-', self.titulo.lower())
        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo
