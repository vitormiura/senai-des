from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def produtos_listar(request):
    if request.method == 'GET':
        #listar os produtos cadastrados invés do OK
        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def produto_detalhes(request, id):
    # try:
        # produto = Produto.objects.get(pk=id)
    produto = get_object_or_404(Produto, pk=id)
    serializer = ProdutoSerializer(produto)
    return Response(serializer.data)
    # except Produto.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)