from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import AccountInfoSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import AccountInfo

class ProfileGetView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AccountInfoSerializer
    queryset = AccountInfo.objects.all()

class ProfilePostView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self,rq):
        print(rq.user)
        print("Data:-",rq.data)
        
        accser = AccountInfoSerializer(data=rq.data,context={"request":rq})
        if accser.is_valid():
            accser.save(user = rq.user)
            return Response(accser.data,status=201)
        else:
            return Response(accser.errors,status=400)
       