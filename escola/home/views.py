from django.shortcuts import render, get_object_or_404, redirect

def home_index(request):
    return render(request, 'home/index.html')