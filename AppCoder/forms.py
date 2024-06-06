from django import forms
from .models import Curso, Profesor

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    cursos = forms.ModelMultipleChoiceField(queryset=Curso.objects.all(), widget=forms.SelectMultiple)

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesores = forms.ModelMultipleChoiceField(queryset=Profesor.objects.all(), widget=forms.SelectMultiple)
    cursos = forms.ModelMultipleChoiceField(queryset=Curso.objects.all(), widget=forms.SelectMultiple)