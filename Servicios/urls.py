
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.servicios, name="Servicios"), # Ahora apunta a la raíz
]

