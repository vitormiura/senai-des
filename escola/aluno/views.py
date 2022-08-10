from django.shortcuts import render
from aluno.models import Aluno


def aluno_index(request):
    aluno_sql = Aluno.objects.all()
    context = {
        'alunos': aluno_sql
    }

    return render(request, 'aluno/index.html', context)
