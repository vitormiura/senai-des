from urllib import response
from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def produtos_listar(request):
    return Response('ok')

@api_view()
def produto_detalhes(request, id):
    return Response(id)