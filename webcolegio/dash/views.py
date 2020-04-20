from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

# Create your views here.


@method_decorator(login_required, name='dispatch')
class HomeTemplateView(TemplateView):
    template_name = 'dash/home.html'


@method_decorator(login_required, name='dispatch')
class SinPermisosTemplateView(TemplateView):
    template_name = 'dash/sinpermisos.html'


class MixinFormInvalid:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


@method_decorator(login_required, name='dispatch')
class SinPermisos(PermissionRequiredMixin, SuccessMessageMixin, MixinFormInvalid):
    raise_exception = False
    redirect_field_name = 'redirect_to'

    def handle_no_permission(self):
        self.login_url = 'sin_permisos'
        return HttpResponseRedirect(reverse_lazy(self.login_url))
