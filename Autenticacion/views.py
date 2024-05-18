from django.shortcuts import redirect, render
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

# USUARIOS POR PRIMERA VEZ.
class VRegistro(View):  
    def get(self, request): # Para enviar el formulario. El orden de self y request es importante
      form=UserCreationForm()
      return render(request, "Registro/registro.html", {"form_tmp":form}) 
        
    def post(self, request):
      form=UserCreationForm(request.POST)
      if form.is_valid():
         usuario=form.save()
         login(request, usuario)
         return redirect("TA_Inicio")
      else:
         for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])
         return render(request, "Registro/registro.html", {"form_tmp":form})
      
def cerrar_sesion(request):
    logout(request)
    return redirect("TA_Inicio")

# USUARIOS YA REGISTRADOS   
def logear(request):
    if request.method == "POST": # VC-64
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username") # cuadro del nombre por defecto.
            contra= form.cleaned_data.get("password") # cuadro del nombre por defecto.
            usuario =authenticate(username= nombre_usuario, password= contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("TA_Inicio")
            else:
                messages.error(request, "Usuario NO válido")
        else:
            messages.error(request, "Autenticación Incorrecta")
    form = AuthenticationForm()
    return render(request, "Login/login.html", {"form": form})