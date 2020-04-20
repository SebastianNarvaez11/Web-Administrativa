from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Circular
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CircularForm
from django.urls import reverse_lazy
# Create your views here.


def blog(request):
    queryset = request.GET.get("buscar")
    lista_posts = Circular.objects.all().order_by('-creacion')
    if queryset:
        lista_posts = Circular.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(lista_posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/blog.html', {'lista_posts': lista_posts, 'posts': posts})


def detallepost(request, pk):
    post = get_object_or_404(Circular, id=pk)
    posts = Circular.objects.all()
    return render(request, 'blog/detallepost.html', {'post': post, 'lista_posts': posts,})