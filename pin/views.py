from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  generics
from .serializers import  PinSerializer
from .models import  Pin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response


class PinListView(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self,rq):
        pin_ser = PinSerializer(data=rq.data)
        if pin_ser.is_valid():
            pin_ser.save(user = rq.user)
            return  Response(pin_ser.data,status=201)
        else:
            return  Response(pin_ser.errors,status=400)
