from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.docentes, name='docentes'),
]

materia_urldash = ([
    path('list/', MateriaListView.as_view(), name='list'),
    path('create/', MateriaCreateView.as_view(), name='create'),
    path('update/<int:pk>', MateriaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MateriaDeleteView.as_view(), name='delete'),
], 'materia_urldash')

docente_urldash = ([
    path('list/', DocenteListView.as_view(), name='list'),
    path('create/', DocenteCreateView.as_view(), name='create'),
    path('update/<int:pk>', DocenteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DocenteDeleteView.as_view(), name='delete'),
], 'docente_urldash')
