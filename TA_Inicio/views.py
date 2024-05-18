from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.

def ta_inicio(request):
    return render(request, "TA_Inicio/ta_inicio.html")
