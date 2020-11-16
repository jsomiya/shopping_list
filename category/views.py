from django.shortcuts import render
from rest_framework import generics
# from rest_framework.response import Response
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Category, Item_List
from .serializers import CategorySerializer, ItemSerializer

# Create your views here.

# @api_view(['POST'])
# def category(category):
#     category = Category.objects.create(category=category)
#     serializer = CategorySerializer(category)
#     return serializer.data

class CategoryAPI(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# @api_view(['POST'])
# def add_item(request):
#     item = Item_List.objects.create(item)
#     serializer = ItemSerializer(item)
#     return serializer.data

class ItemAPI(generics.ListCreateAPIView):
    queryset = Item_List.objects.all()
    serializer_class = ItemSerializer

def 