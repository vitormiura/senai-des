from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item, User
from .serializers import ItemSerializer, userSerializer
from api import serializers

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getUser(request):
    users = User.objects.all()
    serializer = userSerializer(users, many=True)
    return Response(serializer.data) 

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['POST'])
def addUser(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
