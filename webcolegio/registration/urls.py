from django.urls import path
from .views import SignUpView, UsuarioListView, UserPermisionUpdateView, ProfileUpdateView, UserUpdateView, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('profile/', ProfileUpdateView.as_view(), name='perfil')
]

user_urldash = ([
    path('list/', UsuarioListView.as_view(), name='list'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('update_permission/<int:pk>/', UserPermisionUpdateView.as_view(), name='update_permission'),
], 'user_urldash')
