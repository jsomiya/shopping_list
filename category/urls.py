from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPI, ItemAPI, get_count

urlpatterns = [
    path('category/<str:category>/', CategoryAPI.as_view()),
    path('category/<str:category>/items/<str:item>/', ItemAPI.as_view()),
    path('category/items/get_count/', get_count),
]
