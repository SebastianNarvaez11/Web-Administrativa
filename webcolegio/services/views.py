from django.shortcuts import render, get_object_or_404
from .models import Service
from django.views.generic import ListView, CreateView, UpdateView
from .forms import ServiceForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
# Create your views here.


def services(request):
    servicios = Service.objects.filter(estado=True)
    return render(request, 'services/services.html', {'lista_servicios': servicios})


def detalleservicio(request, slug_servicio):
    service = get_object_or_404(Service, slug=slug_servicio)
    return render(request, 'services/detalleservicio.html', {'servicio': service})

#--------------------Vistas Del Dashboard-----------------------#


@method_decorator(login_required, name='dispatch')
class ServiceListView(SinPermisos, ListView):
    permission_required = 'services.view_service'
    model = Service


@method_decorator(login_required, name='dispatch')
class ServiceCreateView(SinPermisos, CreateView):
    permission_required = 'services.add_service'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services_dash:list')
    success_message = 'Servicio creado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class ServiceUpdateView(SinPermisos, UpdateView):
    permission_required = 'services.change_service'
    model = Service
    form_class = ServiceForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('services_dash:list')
    success_message = 'Servicio actualizado satisfactoriamente'
