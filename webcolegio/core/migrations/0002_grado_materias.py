# Generated by Django 2.2.3 on 2019-11-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(related_name='obtener_asignaturas', to='docentes.Materia', verbose_name='Asignaturas que ve'),
        ),
    ]
