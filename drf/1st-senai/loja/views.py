# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer, ProdAdd


@api_view(['POST'])
def addProd(request):
    serializer = ProdAdd(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def produtos_listar(request):
    # if request.method == 'GET':
        queryset = Produto.objects.all().values()
        serializer = ProdutoSerializer(queryset, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = ProdutoSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response('ok')

@api_view(['GET'])
def produto_detalhes(request, id):
    # try:
        # prod = Produto.objects.get(pk=id)
        prod = get_object_or_404(Produto, pk=id)
        serializer = ProdutoSerializer(prod)
        return Response(serializer.data)
    # except Produto.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)