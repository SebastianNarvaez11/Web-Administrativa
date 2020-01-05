from django.urls import path
from .import views
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, PostListView, PostCreateView, PostUpdateView, pdiListView

urlpatterns = [
    path('', views.blog, name='blog'),
]

category_urldash = ([
    path('list/', CategoryListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
], 'category_dash')

post_urldash = ([
    path('list/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
], 'post_dash')

pdi_urldash = ([
    path('', pdiListView.as_view(), name='pdi'),
    path('materias/<int:id_grado>/', views.materias, name='materias'),
    path('post/<int:id_materia>/<int:id_grado>/', views.postMateria, name='posts_materias'),
    path('post/<slug:slug_post>/', views.detallepost, name='detallepost'),
], 'pdi_urldash')
