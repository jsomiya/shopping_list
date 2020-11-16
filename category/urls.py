from django.contrib import admin
from django.urls import path, include
from .views import CategoryAPI, ItemAPI

urlpatterns = [
    # path('category/api/<str:category>/', category , name = 'category'),
    path('category/<str:category>/', CategoryAPI.as_view()),
    # path('category/<str:category>/items/<str:item>', add_item, name = 'add_item'),
    path('category/<str:category>/items/<str:item>', ItemAPI.as_view()),
]
