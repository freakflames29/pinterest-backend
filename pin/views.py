from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  generics
from .serializers import  PinSerializer
from .models import  Pin
class PinListView(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
