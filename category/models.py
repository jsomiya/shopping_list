from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length = 20)

class Item_List(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    item = models.CharField(max_length = 30)

