from django.shortcuts import render, redirect
from .models import Colegio, Grado
from .forms import ColegioForm, GradoForm
from services.models import Service
from django.views.generic import CreateView, UpdateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from dash.views import SinPermisos
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    if not Colegio.objects.all():
        Colegio.objects.create(nombre='', lema='', logo='null',
                               email='', direccion='', telefono='',
                               horarios='', mision='', vision='',
                               historia='', creacion='', edicion='')
        return redirect('colegio_urldash:create', pk=1)

    servicios = Service.objects.filter(index=True)
    return render(request, 'core/index.html', {'lista_servicios': servicios})


def about(request):
    return render(request, 'core/about.html')

####################################### Vistas del Dashboard #############################################

# Vista para actualizar la informacion del colegio
@method_decorator(login_required, name='dispatch')
class ColegioUpdateView(SinPermisos, UpdateView):
    permission_required = 'core.change_colegio'
    model = Colegio
    form_class = ColegioForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')
    success_message = 'Datos actualizados satisfactoriamente'

# vista para crear/actualizar el colegio,(ya que se crea un objeto colegio por defecto) en caso de que no exita
# la vista simula la creacion del colegio
@method_decorator(login_required, name='dispatch')
class ColegioUpdateCreate(SinPermisos, UpdateView):
    model = Colegio
    form_class = ColegioForm
    success_url = reverse_lazy('home')
    template_name = 'core/colegio_form.html'
    success_message = 'Datos creados satisfactoriamente'


################################# Grado Dashboard ######################################
@method_decorator(login_required, name='dispatch')
class GradosListView(SinPermisos, ListView):
    permission_required = 'core.view_grado'
    model = Grado


@method_decorator(login_required, name='dispatch')
class GradoCreateView(SinPermisos, CreateView):
    permission_required = 'core.add_grado'
    model = Grado
    form_class = GradoForm
    success_message = 'Grado creado satisfactoriamente'
    success_url = reverse_lazy('grado_urldash:list')


@method_decorator(login_required, name='dispatch')
class GradoUpdateView(SinPermisos, UpdateView):
    permission_required = 'core.change_grado'
    model = Grado
    form_class = GradoForm
    template_name_suffix = '_update_form'
    success_message = 'Grado actualizado satisfactoriamente'
    success_url = reverse_lazy('grado_urldash:list')
