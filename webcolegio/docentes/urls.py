from django.urls import path
from .import views
from .views import MateriaListView, MateriaCreateView, MateriaUpdateView, DocenteListView, DocenteCreateView, DocenteUpdateView

urlpatterns = [
    path('', views.docentes, name='docentes'),
]

materia_urldash = ([
    path('list/', MateriaListView.as_view(), name='list'),
    path('create/', MateriaCreateView.as_view(), name='create'),
    path('update/<int:pk>', MateriaUpdateView.as_view(), name='update'),
], 'materia_urldash')

docente_urldash = ([
    path('list/', DocenteListView.as_view(), name='list'),
    path('create/', DocenteCreateView.as_view(), name='create'),
    path('update/<int:pk>', DocenteUpdateView.as_view(), name='update'),
], 'docente_urldash')
