"""webcolegio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from services.urls import services_urldash
from pdi.urls import category_urldash, post_urldash, pdi_urldash
from docentes.urls import materia_urldash, docente_urldash
from core.urls import colegio_urldash, grado_urldash
from social.urls import link_urldash
from registration.urls import user_urldash

urlpatterns = [
    # url la app de core
    path('', include('core.urls')),
    # url dashboard
    path('dashboard/', include('dash.urls')),
    path('dashboard/colegio/', include(colegio_urldash)),
    path('dashboard/grados/', include(grado_urldash)),
    path('dashboard/category/', include(category_urldash)),
    path('dashboard/post/', include(post_urldash)),
    ##url blog
    path('blog/', include('blog.urls')),
    # url pdi
    path('pdi/', include(pdi_urldash)),
    # url la app de services
    path('services/', include('services.urls')),
    path('dashboard/services/', include(services_urldash)),
    # url de la app docentes
    path('docentes/', include('docentes.urls')),
    path('dashboard/materias/', include(materia_urldash)),
    path('dashboard/docentes/', include(docente_urldash)),
    # url de la app contacto
    path('contact/', include('contact.urls')),
    # url app social
    path('dashboard/redes/', include(link_urldash)),
    # url lista de usuarios
    path('dashboard/users/', include(user_urldash)),
    # url de admin
    path('admin/', admin.site.urls),
    # url de autenticacion
    path('accounts/', include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    