
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.contacto, name="Contacto"), # Ahora apunta a la raíz
]

