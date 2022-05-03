from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from Shopping.forms import Formulario
from Shopping.models import *


def locales(request):
    return render(request,"Shopping/locales.html")

def patioComidas(request):
    return render(request,"Shopping/patioComidas.html")

def cine(request):
    return render(request,"Shopping/cine.html")

def promociones(request):
    return render(request,"Shopping/promociones.html")

def inicio(request):
    return render(request,"Shopping/inicio.html")

def registro(request):
    return render(request,"Shopping/registro.html")


def formulario(request):
    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            name= Usuarios(nombre=request.POST['nombre'], edad=request.POST['edad'], email=request.POST['email'])
            
            name.save()
           
            return render(request, "Shopping/inicio.html")
    
    else:
        miFormulario=Formulario()
   
    return render(request, "Shopping/formulario.html", {"miFormulario":miFormulario})

def busquedaUsuario(request):
    if request.GET["usuario"]:
        usuario= request.GET['usuario']
        registros = Usuarios.objects.filter(nombre__icontains=usuario)

        return render(request, "Shopping/resultadosBusqueda.html", {"nombres":usuario, "registros":registros})
    else:

        respuesta="No enviaste datos"

        return HttpResponse(respuesta)
