from django.urls import path
from .import views
from .views import ServiceListView, ServiceCreateView, ServiceUpdateView

urlpatterns = [
    path('', views.services, name='services'),
    path('<slug:slug_servicio>/', views.detalleservicio, name='detalleservicio'),
]

services_urldash = ([
    path('list/', ServiceListView.as_view(), name='list'),
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ServiceUpdateView.as_view(), name='update')
], 'services_dash')
