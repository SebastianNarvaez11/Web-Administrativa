from django.db import models
from django.contrib.auth.models import User

def custom_upload_to(instance, filename):
    old_instance =  Profile.objects.get(pk=instance.pk)
    old_instance.imagen.delete()
    return 'profiles/' + filename
    
    

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)
    imagen = models.ImageField('Foto de perfil', upload_to=custom_upload_to ,blank=True, null=True)
    link = models.URLField('Link', blank= True, null = True)
    info = models.CharField('Informacion', blank=True, null=True, max_length=300)
    edicion = models.DateTimeField('Edicion', auto_now=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return self.user.username

