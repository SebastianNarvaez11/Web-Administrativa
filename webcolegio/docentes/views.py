from django.shortcuts import render
from .models import Docente, Materia
from .forms import MateriaForm, DocenteForm
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.urls import reverse_lazy
# Create your views here.


def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/docentes.html', {'docentes': docentes})


################## Vistas Dashboard Materias ###########################################

@method_decorator(login_required, name='dispatch')
class MateriaListView(SinPermisos, ListView):
    permission_required = 'docentes.view_materia'
    model = Materia


@method_decorator(login_required, name='dispatch')
class MateriaCreateView(SinPermisos, CreateView):
    permission_required = 'docentes.add_materia'
    model = Materia
    form_class = MateriaForm
    success_message = "Asignatura creada satisfactoriamente"
    success_url = reverse_lazy('materia_urldash:list')


@method_decorator(login_required, name='dispatch')
class MateriaUpdateView(SinPermisos, UpdateView):
    permission_required = 'docentes.change_materia'
    model = Materia
    form_class = MateriaForm
    template_name_suffix = '_update_form'
    success_message = "Asignatura actualizada satisfactoriamente"
    success_url = reverse_lazy('materia_urldash:list')

############################## Vistas Dashboard Docente #########################################


@method_decorator(login_required, name='dispatch')
class DocenteListView(SinPermisos, ListView):
    permission_required = 'docentes.view_docente'
    model = Docente


@method_decorator(login_required, name='dispatch')
class DocenteCreateView(SinPermisos, CreateView):
    permission_required = 'docentes.add_docente'
    model = Docente
    form_class = DocenteForm
    success_url = reverse_lazy('docente_urldash:list')
    success_message = "Docente creado satisfactoriamente"

class DocenteUpdateView(SinPermisos, UpdateView):
    permission_required = 'docentes.change_docente'
    model = Docente
    form_class = DocenteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('docente_urldash:list')
    success_message = "Docente actualizado satisfactoriamente"
