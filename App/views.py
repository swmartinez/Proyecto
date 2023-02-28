from django.shortcuts import render
from django.http import HttpResponse

from App.models import Curso

def curso(request):
    curso = Curso(nombre='Backend', camada='12345')
    curso.save()
    respuesta= f'Curso: {curso.nombre}, Camada: {curso.camada}'

    return HttpResponse(respuesta)