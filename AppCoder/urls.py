from django.contrib import admin
from django.urls import path
from AppCoder.views import (
    inicio, 
    cursos, 
    profesores, 
    estudiantes, 
    entregables, 
    curso_formulario,
    busqueda_curso,
    buscar,
    profesor_formulario,
    busqueda_profesor,
    buscar_profesor,
    estudiante_formulario,
    busqueda_estudiante,
    buscar_estudiante
)

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    path('busqueda-curso/', busqueda_curso, name='BusquedaCurso'),
    path('buscar/', buscar, name='BuscarCurso'),

    path('profesores/', profesores, name='Profesores'),
    path('profesor-formulario/', profesor_formulario, name='ProfesorFormulario'),
    path('busqueda-profesor/', busqueda_profesor, name='BusquedaProfesor'),
    path('buscar-profesor/', buscar_profesor, name='BuscarProfesor'),

    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('estudiante-formulario/', estudiante_formulario, name='EstudianteFormulario'),
    path('busqueda-estudiante/', busqueda_estudiante, name='BusquedaEstudiante'),
    path('buscar-estudiante/', buscar_estudiante, name='BuscarEstudiante'),

    path('entregables/', entregables, name='Entregables'),
]
