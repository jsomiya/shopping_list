from django.shortcuts import render
from rest_framework import generics
# from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
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

def get_count(request):
    item = Item_List.objects.all()
    item_list = []
    for i in item:
        serializer = ItemSerializer(i.item, many= False)
        j = i.item
        item_list.append(j)
    # print(item_list)
    item_list = list(set(item_list))
    # print(item_list)
    t = len(item_list)
    # print(t)
    return HttpResponse(t,status = status.HTTP_200_OK)
