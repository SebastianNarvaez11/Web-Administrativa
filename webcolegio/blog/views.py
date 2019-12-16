from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from core.models import Grado
from docentes.models import Materia
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CategoryForm, PostForm
from django.urls import reverse_lazy
# Create your views here.


def blog(request):
    queryset = request.GET.get("buscar")
    lista_posts = Post.objects.all()
    if queryset:
        lista_posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(lista_posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    categorias = Category.objects.all()
    grados = Grado.objects.all()
    return render(request, 'blog/blog.html', {'lista_posts': lista_posts, 'categorias': categorias, 'posts': posts, 'grados': grados})


def detallepost(request, slug_post):
    post = get_object_or_404(Post, slug=slug_post)
    posts = Post.objects.all()
    categorias = Category.objects.all()
    grados = Grado.objects.all()
    return render(request, 'blog/detallepost.html', {'post': post, 'lista_posts': posts, 'categorias': categorias, 'grados': grados})


def postMateria(request, id_materia, id_grado):
    materia = get_object_or_404(Materia, id=id_materia)
    grado = get_object_or_404(Grado, id=id_grado)
    lista_posts = Post.objects.filter(materia=materia, grado=grado)

    paginator = Paginator(lista_posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/blog_filter.html', {'posts': posts, 'grado': grado, 'materia': materia})


def materias(request, id_grado):
    grado = get_object_or_404(Grado, id=id_grado)
    return render(request, 'blog/materias.html', {'grado': grado})


######## Vistas Del Dashboard Categoria #########################
@method_decorator(login_required, name='dispatch')
class CategoryListView(SinPermisos, ListView):
    permission_required = 'blog.view_category'
    model = Category


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(SinPermisos, CreateView):
    permission_required = 'blog.add_category'
    model = Category
    form_class = CategoryForm
    success_message = "Categoria creada satisfactoriamente"
    success_url = reverse_lazy('category_dash:list')


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(SinPermisos, UpdateView):
    permission_required = 'blog.change_category'
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_update_form'
    success_message = "Categoria actualizada satisfactoriamente"
    success_url = reverse_lazy('category_dash:list')


######## Vistas Del Dashboard Post #########################
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post

    # filtra el el queryset por autor, solo podra ver los post que sean de su propiedad
    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)


@method_decorator(login_required, name='dispatch')
class PostCreateView(SinPermisos, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_dash:list')
    success_message = "Post creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(SinPermisos, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
    success_message = "Post actualizado satisfactoriamente"
    success_url = reverse_lazy('post_dash:list')

    # filtra el el queryset por autor, solo podra editar los post que sean de su propiedad
    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class pdiListView(ListView):
    model = Grado
    template_name = 'blog/homepdi.html'
