from django.urls import path
from .views import HomeTemplateView, SinPermisosTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('sinpermisos/', SinPermisosTemplateView.as_view(), name='sin_permisos'),
]
