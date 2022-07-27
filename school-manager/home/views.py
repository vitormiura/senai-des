
from django.shortcuts import render, HttpResponse

from home.models import Curso


def home_index(request):
    dados = Curso.objects.all() 
    context={
        'curso' : dados
    }

    return render(request, 'home/index.html', context)

def home_detalhes(request, id):
    data = Curso.objects.get(id = id)
    return render(request, 'home/detalhes.html', {'curso' : data})
