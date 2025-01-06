from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import AccountInfoSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import AccountInfo
from django.db.utils import IntegrityError
from .permissions import IsOwner

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
        
        try:
            accser = AccountInfoSerializer(data=rq.data,context={"request":rq})
            if accser.is_valid():
                accser.save(user = rq.user)
                return Response(accser.data,status=201)
            else:
                return Response(accser.errors,status=400)
        except IntegrityError as ie:
            return Response({"error":"You already created the profile"},status=400)
        except:
            return Response({"error":"Something went wrong"},status=400)

class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [JWTAuthentication]
    def patch(self,rq,pk):
        try:
            profile = AccountInfo.objects.get(pk=pk)
            
            try:
                self.check_object_permissions(rq,profile)
            except:
                return Response({"error":"You dont have persimssion for this profile"},status=403)
            profile_ser = AccountInfoSerializer(profile,data=rq.data,partial=True,context={"request":rq})
            if profile_ser.is_valid():
                profile_ser.save()
                return Response(profile_ser.data,status=201)
            else:
                return Response(profile_ser.errors,status=400)
            
            
        except AccountInfo.DoesNotExist as e:
            print("*"*10,e)
            return Response({"error":"Profile not found"},status=404)
        except Exception as e:
            return Response({"error":"Something went wrong"},status=400)
            
