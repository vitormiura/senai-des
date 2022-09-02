from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto, Pedido, PedidoItem, Cliente
from .serializer import ProdutoSerializer, PedidoSerializer, ClienteSerializer, ItemSerializer
from rest_framework import status, generics

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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def produto_detalhes(request, id):
    # try:
        # produto = Produto.objects.get(pk=id)
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # except Produto.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)

class PedidoList(generics.ListCreateAPIView):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        queryset = Pedido.objects.all()
        item = self.request.query_params.get('item')
        client = self.request.query_params.get('client')

        if item and client is not None:
            queryset = queryset.filter(items = item, cliente = client)
        return queryset

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class ClientList(generics.ListCreateAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = PedidoItem.objects.all()

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = PedidoItem.objects.all()
