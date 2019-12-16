# Generated by Django 2.2.3 on 2019-10-24 00:24

import ckeditor.fields
from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20, unique=True, verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Slug/Url')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('mensualidad', models.IntegerField(verbose_name='Mensualidad')),
                ('matricula', models.IntegerField(verbose_name='Matricula')),
                ('imagen', models.ImageField(upload_to=services.models.custom_upload_to, verbose_name='Imagen')),
                ('jornada', models.CharField(blank=True, max_length=80, null=True, verbose_name='Jornada(s)')),
                ('index', models.BooleanField(default=True, verbose_name='Mostrar en el inicio')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/Oculto')),
                ('creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('edicion', models.DateField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-creacion'],
            },
        ),
    ]
