from django.urls import path
from .import views
#from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, PostListView, PostCreateView, PostUpdateView, pdiListView


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.detallepost, name='detallepost'),
]