from rest_framework import serializers
from base.models import Item, User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        