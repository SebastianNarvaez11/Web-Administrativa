from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from core.validators import *


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=20, required=True, validators=[validate_only_letters])
    last_name = forms.CharField(max_length=20, required=True, validators=[validate_only_letters])
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'groups', 'is_active']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            username = self.cleaned_data.get("username")
            if not user.username == username:
                raise forms.ValidationError(
                    "El email ya existe, prueba con otro")

        return email


class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=15, min_length=5)
    first_name = forms.CharField(max_length=20, required=True, validators=[validate_only_letters])
    last_name = forms.CharField(max_length=20, required=True, validators=[validate_only_letters])
    email = forms.EmailField(max_length=254, required=True)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        #comprobamos si el campo email se ah modificado
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "El email ya existe, prueba con otro")

        return email


class UserPermisionForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['groups', 'is_active']


class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['imagen', 'info', 'link']


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.is_active:
                return username
            else:
                raise forms.ValidationError(
                    "su usuario esta inactivo, comuniquese con el administrador")

        return username
