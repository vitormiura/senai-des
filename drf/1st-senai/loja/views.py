from urllib import response
from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer

@api_view()
def produtos_listar(request):
    return Response('ok')

@api_view(['GET'])
def produto_detalhes(request, id):
    prod = Produto.objects.get(pk=id)
    serializer = ProdutoSerializer(prod)
    
    return Response(serializer.data)