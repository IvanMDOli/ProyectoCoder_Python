from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from .forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario

# Create your views here.

def inicio(req):

    return render(req, "inicio.html", {})

def cursos(req):

    cursos = Curso.objects.all()

    return render(req, "cursos.html", {"lista_cursos": cursos})

def profesores(req):

    profesores = Profesor.objects.all()

    return render(req, "profesores.html", {"profesores": profesores})

def profesor_formulario(req):

    if req.method == 'POST':

        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            
            nombre = miFormulario.cleaned_data['nombre']
            apellido = miFormulario.cleaned_data['apellido']
            email = miFormulario.cleaned_data['email']
            profesion = miFormulario.cleaned_data['profesion']
            cursos = miFormulario.cleaned_data['cursos']

            nuevo_profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            nuevo_profesor.save()
            nuevo_profesor.cursos.set(cursos)

            return render(req, "inicio.html", {"message": "Profesor creado con éxito"})
        else:

            return render(req, "inicio.html", {"message": "Datos Invalidos"})
    else:

        miFormulario = ProfesorFormulario()
        return render(req, "profesor_formulario.html", {"miFormulario": miFormulario})

def busqueda_profesor(req):

    return render(req, "busqueda_profesor.html", {})    

def estudiantes(req):

    estudiantes = Estudiante.objects.all()

    return render(req, "estudiantes.html", {"estudiantes": estudiantes})

def estudiante_formulario(req):

    if req.method == 'POST':

        miFormulario = EstudianteFormulario(req.POST)

        if miFormulario.is_valid():
            
            nombre = miFormulario.cleaned_data['nombre']
            apellido = miFormulario.cleaned_data['apellido']
            email = miFormulario.cleaned_data['email']
            profesores = miFormulario.cleaned_data['profesores']
            cursos = miFormulario.cleaned_data['cursos']

            nuevo_estudiantes = Estudiante(nombre=nombre, apellido=apellido, email=email)
            nuevo_estudiantes.save()
            nuevo_estudiantes.cursos.set(cursos)
            nuevo_estudiantes.profesores.set(profesores)
            return render(req, "inicio.html", {"message": "Estudiante creado con éxito"})
        else:

            return render(req, "inicio.html", {"message": "Datos Invalidos"})
    else:

        miFormulario = EstudianteFormulario()
        return render(req, "estudiante_formulario.html", {"miFormulario": miFormulario})

def busqueda_estudiante(req):

    return render(req, "busqueda_estudiante.html", {})    

def entregables(req):

    return render(req, "entregables.html", {})

def curso_formulario(req):

    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()

            return render(req, "inicio.html", {"message": "Curso creado con éxito"})
        
        else:

            return render(req, "inicio.html", {"message": "Datos Invalidos"})
    
    else:

        miFormulario = CursoFormulario()
        return render(req, "curso_formulario.html", {"miFormulario": miFormulario})
    
def busqueda_curso(req):

    return render(req, "busqueda_curso.html", {})

def buscar (req):

    if req.GET["camada"]:

        camada = req.GET["camada"]

        try:
            curso = Curso.objects.get(camada=camada)
            return render(req, "resultado_busqueda.html", {"curso": curso, "camada": camada})
        
        except:
            return render(req, "inicio.html", {"message": "La camada no existe"})
        
def buscar_profesor (req):

    if req.GET["nombre_profesor"]:

        nombre = req.GET["nombre_profesor"]
        
        try:
            profesor = Profesor.objects.get(nombre=nombre)
            return render(req, "resultado_busqueda.html", {"profesor": profesor})
        
        except:
            return render(req, "inicio.html", {"message": "El profesor no existe"}) 

def buscar_estudiante (req):

    if req.GET["nombre_estudiante"]:

        nombre = req.GET["nombre_estudiante"]

        try:
            estudiante = Estudiante.objects.get(nombre=nombre)
            return render(req, "resultado_busqueda.html", {"estudiante": estudiante})
        
        except:
            return render(req, "inicio.html", {"message": "El estudiante no existe"})        