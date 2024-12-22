from django.shortcuts import render
from .serializers import  BoardSerializer
from .models import Board
from rest_framework import generics
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import  JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class BoardView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,rq):
        user = rq.user
        print(f"{user} (*(**(*(*(*(*(*(*(*")

        boards = user.boards
        boards_ser = BoardSerializer(boards,many=True)
        return  Response(boards_ser.data,status=200)

    def post(self,rq):
        print(f"{rq.data}----------------------")
        board_ser = BoardSerializer(data=rq.data)
        if board_ser.is_valid():
            board_ser.save(user = rq.user)
            return  Response(board_ser.data,status=201)
        else:
            return  Response(board_ser.errors,status=400)


class BoardSingleView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    serializer_class = BoardSerializer
    queryset = Board.objects.all()
