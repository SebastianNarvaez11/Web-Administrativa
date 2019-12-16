from django.urls import path
from .import views
from .views import ColegioUpdateCreate, ColegioUpdateView, GradosListView, GradoCreateView, GradoUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

colegio_urldash = ([
    path('create/<int:pk>/', ColegioUpdateCreate.as_view(), name='create'),
    path('update/<int:pk>/', ColegioUpdateView.as_view(), name='update'),
], 'colegio_urldash')

grado_urldash = ([
    path('list/', GradosListView.as_view(), name='list'),
    path('create/', GradoCreateView.as_view(), name='create'),
    path('update/<int:pk>', GradoUpdateView.as_view(), name='update'),
], 'grado_urldash')
