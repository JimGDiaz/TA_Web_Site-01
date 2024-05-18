
from django.urls import path
#from . import views
from .views import VRegistro
from .views import VRegistro, cerrar_sesion, logear

urlpatterns = [
    
    #path('', views.autenticacion, name="Autenticacion"), # Ahora apunta a la raíz
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="Logear"),
]

