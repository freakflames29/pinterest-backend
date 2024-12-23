from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status


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

        except Exception as e:
            print("Error is ", e)
            return Response({"error": "Username, password , email required"}, status=400)
