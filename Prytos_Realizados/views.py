from django.shortcuts import render
from Prytos_Realizados.models import Uso_Edif, Prytos_Realizados
# Create your views here.

def prytos_realizados(request): # Nombre del id en la tabla
    prytos_usos = Prytos_Realizados.objects.all() # Todos los proyectos con todos los Usos
    return render(request, "Prytos_Realizados/prytos_realizados.html", {"prytos_tmp":prytos_usos})


def uso_Edif(request, prytos_id ):
    usos_Edif= Uso_Edif.objects.get(id=prytos_id)
    prytos_f = Prytos_Realizados.objects.filter(usos_Edif)
    return render(request, "Prytos_Realizados/uso_edif.html", {"usos_tmp": usos_Edif, "prytos_f":prytos_f})
