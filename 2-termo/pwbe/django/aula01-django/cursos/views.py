from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Cursos

# def index(request):
#     return render(request, 'index.html')

# def index(request):
#     cursos = {
#         '1':'Smart',
#         '2':'Manufatura',
#         '3':'Mecatrônica',
#         '4':'Adm'
#     }

#     dados = {
#         'nome_cursos' : cursos
#     }

#     return render(request, 'index.html', dados)

def index(request):
    cursos = Cursos.objects.all()
    dados = {
        'cursos':cursos
    }
    return render(request, 'index.html', dados)

def cursos(request, curso_id):
    curso = get_object_or_404(Cursos, pk = curso_id)
    curso_a_ser_exibido={
        'curso' : curso
    }
    return render(request, 'curso.html', curso_a_ser_exibido)