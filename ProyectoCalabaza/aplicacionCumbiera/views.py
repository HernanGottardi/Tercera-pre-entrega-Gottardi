from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from .forms import *

#------------------------------------------
#------------------------------------------
#------------------------------------------

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["comision"]:

        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppCoder/busquedaCamada.html", {"cursos": cursos, "comision": comision})
    else:
        respuesta = "No enviaste datos"
    #respuesta = f"Estoy buscando la com nro: {request.GET['comision']}"
    return HttpResponse(respuesta)

#------------------------------------------
#------------------------------------------
#------------------------------------------
def profesores(request):
    if(request.method == "POST"):
        form = ProfesorForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesion = form.cleaned_data['profesion']

            profesor = Profesor()
            profesor.nombre = nombre
            profesor.apellido = apellido
            profesor.email = email
            profesor.profesion = profesion

            profesor.save()
            form = ProfesorForm()
    else:
         form = ProfesorForm()
         
    # con esto vamos a tener a todos los profesores guardados en la BBDD.
    profesores = Profesor.objects.all()
    context = {"profesores": profesores, "form": form}

    return render(request, "AppCoder/profesores.html", context)

def estudiantes(request):
    if(request.method == "POST"):
        form = EstudianteForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']

            estudiante = Estudiante()
            estudiante.nombre = nombre
            estudiante.apellido = apellido
            estudiante.email = email

            estudiante.save()
            form = EstudianteForm()
    else:
         form = EstudianteForm()         
    estudiantes = Estudiante.objects.all()
    context = {"Estudiantes": estudiantes, "form": form}
    return render(request, "AppCoder/estudiantes.html", context)

def entregables(request):
    if(request.method == "POST"):
        form = EntregableForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            fecha_entrega = form.cleaned_data['fecha_entrega']
            entregado = form.cleaned_data['entregado']

            entregable = Entregable()
            entregable.nombre = nombre
            entregable.fecha_entrega = fecha_entrega
            entregable.entregado = entregado

            entregable.save()
            form = EntregableForm()
    else:
         form = EntregableForm()         
    entregables = Entregable.objects.all()
    context = {"Entregas": entregables, "form": form}
    return render(request, "AppCoder/entregables.html", context)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    if(request.method == "POST"):
        form = CursoForm(request.POST)
        if form.is_valid():

            nombreCurso = form.cleaned_data['curso']
            comision = form.cleaned_data['comision']

            cursito = Curso()
            cursito.nombre = nombreCurso
            cursito.comision = comision

            cursito.save()
            form = CursoForm()
    else:
         form = CursoForm()         
    cursos = Curso.objects.all()
    context = {"Cursos": cursos, "form": form}
 
    return render(request, "AppCoder/cursos.html", context)
