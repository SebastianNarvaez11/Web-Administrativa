from django.urls import path
from .import views
from .views import CircularListView, CircularCreateView, CircularUpdateView, CircularDeleteView


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.detallepost, name='detallepost'),
]

blog_urldash = ([
    path('list/', CircularListView.as_view(), name='list'),
    path('create/', CircularCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CircularUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CircularDeleteView.as_view(), name='delete'),
], 'blog_dash')