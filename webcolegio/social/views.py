from django.shortcuts import render
from .models import Link
from .forms import LinkForm
from django.views.generic import ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.urls import reverse_lazy

# Create your views here.


@method_decorator(login_required, name='dispatch')
class LinkListView(SinPermisos, ListView):
    permission_required = 'social.view_link'
    model = Link


@method_decorator(login_required, name='dispatch')
class LinkUpdateView(SinPermisos, UpdateView):
    permission_required = 'social.change_link'
    model = Link
    form_class = LinkForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('link_urldash:list')
    success_message = 'Enlace actualizado satisfactoriamente'

    def get_success_url(self):
        return reverse_lazy('link_urldash:list') + '?updated'
