from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
     # Instanciar la Clase del Formulario
     formulario_contacto = FormularioContacto()
     
     if request.method == "POST":
          formulario_contacto=FormularioContacto(data=request.POST)
          if formulario_contacto.is_valid(): # Recarga por el método GET
               nombre=request.POST.get("nombre")
               email=request.POST.get("email")
               contenido=request.POST.get("contenido")
               email=EmailMessage("Mensaje desde App Django", "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), "", ["jamespmcneutron@gmail.com"], reply_to=[email])
               
               try:
                    email.send()
                    return redirect("/contacto/?valido")
               except:
                    return redirect("/contacto/?novalido")
          
     return render(request, "Contacto/contacto.html", {"mi_formulario":formulario_contacto})

