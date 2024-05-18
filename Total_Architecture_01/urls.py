"""
URL configuration for Total_Architecture_01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from ast import Import
from pydoc import resolve
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TA_Inicio.urls')),
    path('autenticacion/', include('Autenticacion.urls')),
    path('blog/', include('Blog.urls')), # Coloque el slash para que funcione la ruta siguiente
    path('contacto/', include('Contacto.urls')), # Coloque el slash para que funcione la rutaPIP
    path('prytos_realizados/', include('Prytos_Realizados.urls')),
    path('servicios', include('Servicios.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 