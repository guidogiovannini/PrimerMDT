from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import familiares
# Create your views here.
def familiarestemp(request):
    #plantilla=loader.get_template("template1.html")
    listafam = familiares.objects.all()
    Context = {'listafam':listafam}
    #contexto = Context(listafam)
    #documento=plantilla.render()
    return render(request, "template1.html", Context)

def agregar(request):
    Nombre = request.POST["Nombre"]
    Apellido = request.POST["Apellido"]
    Edad = request.POST["Edad"]
    Parentesco = request.POST["Parentesco"]
    addfam = familiares(Nombre=Nombre, Apellido=Apellido, Edad=Edad, Parentesco=Parentesco)
    addfam.save()
    return redirect('/desafio/')

def borrar(request, id):
    borrar_fam = familiares.objects.get(id=id)
    borrar_fam.delete()
    return redirect('/desafio/')
