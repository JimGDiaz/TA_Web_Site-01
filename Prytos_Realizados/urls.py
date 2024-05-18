
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.prytos_realizados, name="Prytos_Realizados"), # Ahora apunta a la raíz
    path('uso_Edif/<int:uso_Edif_id>/', views.uso_Edif, name= "uso_Edif"),
    
] 
    
    # path('uso_Edif/<int:uso_Edif_id>/', views.uso_Edif, name= "uso_Edif"),