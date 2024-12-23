from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import PinSerializer
from .models import Pin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.authentication import BasicAuthentication
from rest_framework import  mixins
from .permissions import IsUser

class PinListView(generics.ListAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title"]


class PinCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = PinSerializer
    queryset = Pin.objects.all()

    # def post(self, rq):
    #     pin_ser = PinSerializer(data=rq.data)
    #     if pin_ser.is_valid():
    #         pin_ser.save(user=rq.user)
    #         return Response(pin_ser.data, status=201)
    #     else:
    #         return Response(pin_ser.errors, status=400)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# list pin based on PK
class PinSingleView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsUser]

    serializer_class = PinSerializer
    queryset = Pin.objects.all()

