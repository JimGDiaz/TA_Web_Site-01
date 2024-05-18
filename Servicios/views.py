from django.shortcuts import render
from django.shortcuts import render, HttpResponse

from Servicios.models import Servicios

# Create your views here.

def servicios(request):
    servicios=Servicios.objects.all()
    return render(request, "Servicios/servicios.html",{"servicios_tmp": servicios})
