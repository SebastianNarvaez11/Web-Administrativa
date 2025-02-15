from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Circular
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CircularForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


def blog(request):
    queryset = request.GET.get("buscar")
    lista_posts = Circular.objects.all()
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



######## Vistas Del Dashboard Post #########################
@method_decorator(login_required, name='dispatch')
class CircularListView(ListView):
    model = Circular

    # filtra el el queryset por autor, solo podra ver los post que sean de su propiedad
    def get_queryset(self):
        return Circular.objects.filter(autor=self.request.user)


@method_decorator(login_required, name='dispatch')
class CircularCreateView(SinPermisos, CreateView):
    permission_required = 'blog.add_circular'
    model = Circular
    form_class = CircularForm
    success_url = reverse_lazy('blog_dash:list')
    success_message = "Post creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CircularUpdateView(SinPermisos, UpdateView):
    permission_required = 'blog.change_circular'
    model = Circular
    form_class = CircularForm
    template_name_suffix = '_update_form'
    success_message = "Post actualizado satisfactoriamente"
    success_url = reverse_lazy('blog_dash:list')

    # filtra el el queryset por autor, solo podra editar los post que sean de su propiedad
    def get_queryset(self):
        return Circular.objects.filter(autor=self.request.user)

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CircularDeleteView(SinPermisos, DeleteView):
    permission_required = 'blog.delete_circular'
    model = Circular
    success_url = reverse_lazy('blog_dash:list')
    success_message = "Post eliminado satisfactoriamente"

    # Toca meterle esto devido a un error en django, para que mande el mensaje
    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.imagen.delete()
        messages.success(self.request, self.success_message)
        return super(CircularDeleteView, self).delete(request, *args, **kwargs)