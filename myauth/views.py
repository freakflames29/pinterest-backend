from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db import IntegrityError, Error
from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import ModelSerializer

class UserView(APIView):
    def post(self, rq):
        try:
            username = rq.data['username']
            email = rq.data['email']
            password = rq.data['password']

            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            token = str(AccessToken.for_user(user))

            data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token
            }
            return Response(data, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return Response({"error": "Username already exists"}, status=status.HTTP_401_UNAUTHORIZED)

        except Error as err:
            return Response(
                {"error": err.message},
                status=400
            )
        except Exception as e:
            print("Error is ", e)
            return Response({"error": "Username, password , email required"}, status=400)

class LoginView(APIView):
    def post(self,rq):
        try:
            username = rq.data['username']
            password  = rq.data['password']

            user = authenticate(rq,username=username,password=password)
            if user:
                token = str(AccessToken.for_user(user))
                data = {
                    "id":user.id,
                    "username":user.username,
                    "email": user.email,
                    "token":token

                }
                return Response(data,status=200)
            else:
                return Response({"error":"Username / password is incorrect"},status=400)
        except:
            return  Response({"error":"Username and password is required"},status=400)
