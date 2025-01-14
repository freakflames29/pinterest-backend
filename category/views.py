from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category

from rest_framework import generics

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

