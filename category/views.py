from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from rest_framework.views import APIView
from pin.serializers import PinSerializer
from rest_framework.response import Response

from rest_framework import generics

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategorySinglePinView(APIView):
    def get(self,rq,pk):
        try:
            cat = Category.objects.get(pk=pk)
            pins = cat.pins.all()
            pinser= PinSerializer(pins,many=True,context={"request":rq})
            return Response(pinser.data,status=200)
        except Exception as e:
            print("x"*100,e)
            return Response({"error":"No category found"},status=404)