from django.shortcuts import render

def aluno_index(request):
    return render(request, 'aluno/index.html')
