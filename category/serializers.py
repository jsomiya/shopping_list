from rest_framework import serializers
from .models import Category, Item_List

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_List
        fields = ('id','item','category')