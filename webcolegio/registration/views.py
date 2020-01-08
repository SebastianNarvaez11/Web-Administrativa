from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserPermisionForm, UserUpdateForm, LoginForm, ProfileForm
from django.contrib.auth.models import User, Permission
from .models import Profile
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dash.views import SinPermisos
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse


def login(request):
    # Creamos el formulario de autenticación vacío
    form = LoginForm
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = LoginForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/login.html", {'form': form})


# Create your views here
@method_decorator(login_required, name='dispatch')
class SignUpView(SinPermisos, CreateView):
    permission_required = 'auth.add_user'
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('user_urldash:list')
    success_message = 'Usuario creado satisfactoriamente'

    # funcion le agrega los permisos(grupos) al usuario despues de crearlo
    def form_valid(self, form):
        user = form.save()
        grupos = form.cleaned_data.get("groups")
        for grupo in grupos:
            user.groups.add(grupo)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


@method_decorator(login_required, name='dispatch')
class UserUpdateView(SinPermisos, UpdateView):
    permission_required = 'registration.change_profile'
    model = User
    form_class = UserUpdateForm
    template_name = 'registration/user_update_form.html'
    success_url = reverse_lazy('perfil')
    success_message = 'Datos actualizados satisfactoriamente'

    # obtener objeto que se va a editar para no pasar el id por la url
    def get_object(self):
        user = self.request.user
        return user


class UserPermisionUpdateView(SinPermisos, UpdateView):
    permission_required = 'auth.change_user'
    model = User
    form_class = UserPermisionForm
    template_name = 'registration/userpermision_update_form.html'
    success_url = reverse_lazy('user_urldash:list')
    success_message = 'Permisos actualizados satisfactoriamente'

    # funcion le cambia los permisos(grupos) al usuario despues de actualizarlo
    def form_valid(self, form):
        user = form.save()
        grupos = form.cleaned_data.get("groups")
        user.groups.set(grupos)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UsuarioListView(SinPermisos, ListView):
    permission_required = 'auth.view_user'
    model = User
    template_name = 'registration/user_list.html'

    # no mostrar en la lista, ni el usuario actual, ni los super usuarios
    def get_queryset(self):
        return User.objects.exclude(is_superuser=True).exclude(id=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(SinPermisos, UpdateView):
    permission_required = 'registration.change_profile'
    model = Profile
    form_class = ProfileForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('perfil')
    success_message = 'Perfil actualizado satisfactoriamente'

    # obtener objeto que se va a editar y si no existe lo crea
    def get_object(self):
        profile, create = Profile.objects.get_or_create(user=self.request.user)
        return profile
