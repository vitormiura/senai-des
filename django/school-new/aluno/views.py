from django.contrib import messages
from django.shortcuts import render
from aluno.form import AlunoModelForm, UsuarioModelForm
from aluno.models import Aluno


def aluno_index(request):
    aluno_sql = Aluno.objects.all()
    context = {
        'alunos': aluno_sql
    }
    return render(request, 'aluno/index.html', context)


def aluno_cadastro(request):
    if str(request.method) == 'POST':
        print('Entrou')
        aluno = AlunoModelForm(request.POST)
        if aluno.is_valid():
            aluno.save()
            messages.success(request, 'Salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar')
    else:
        aluno = AlunoModelForm()
    context = {
        'form': aluno
    }
    return render(request, 'aluno/aluno_cadastro.html', context)


def cadastro_usuario(request):
    if str(request.method) == 'POST':
        print('Entrou')
        usuario = UsuarioModelForm(request.POST)
        if usuario.is_valid():
            usuario.save()
            messages.success(request, 'Salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar')
    else:
        usuario = UsuarioModelForm()
    context = {
        'form': usuario
    }
    return render(request, 'aluno/usuario_cadastro.html', context)
