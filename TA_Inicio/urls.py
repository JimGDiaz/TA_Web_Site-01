from django.urls import path
from TA_Inicio import views

from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', views.ta_inicio, name="TA_Inicio"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

