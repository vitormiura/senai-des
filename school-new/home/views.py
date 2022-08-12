from django.shortcuts import render


def index_home(request):
    return render(request, 'home/index.html')
