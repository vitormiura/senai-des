from django.shortcuts import render
from home.models import Agenda

def index(request):
    # dados = Agenda.objects.filter(
    #     price__gte = 23, #MAIORES OU IGUAIS
    #     price__lte = 233, #MENORES OU IGUAIS
    # )

    dados = Agenda.objects.order_by('-id') #Do menor para o maior

    #dados = Agenda.objects.get('id') 

    context = {
        'agenda':dados
    }

    return render(request, 'home/index.html', context)