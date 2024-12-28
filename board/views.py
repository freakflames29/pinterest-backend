from django.shortcuts import render
from .serializers import BoardSerializer
from .models import Board
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from pin.models import  Pin

from pin.serializers import PinSerializer


class BoardView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # serializer_class = BoardSerializer
    # queryset = Board.objects.all()

    def get(self, rq):
        user = rq.user
        print(f"{user} (*(**(*(*(*(*(*(*(*")

        boards = user.boards

        """
        Q:in APIView if im using nested serializers with image field it is showing the relative path not the abosolute path it was starting from /media/ but if i use LISTAPIView it was showing abosulute path
        
        Ans:
            This behavior is because in APIView, the context (which includes the request object) isn't automatically passed to the serializer, but in ListAPIView and other generic views, it is.

            The request object in the serializer's context is crucial for building absolute URLs (e.g., using request.build_absolute_uri), particularly for fields like ImageField
            
            
            
            To make your APIView behave like ListAPIView and generate absolute paths, you need to explicitly pass the request object to the serializer context.
        """

        boards_ser = BoardSerializer(
            boards, many=True, context={"request": rq})
        return Response(boards_ser.data, status=200)

    def post(self, rq):
        print(f"{rq.data}----------------------")
        board_ser = BoardSerializer(data=rq.data)
        if board_ser.is_valid():
            board_ser.save(user=rq.user)
            return Response(board_ser.data, status=201)
        else:
            return Response(board_ser.errors, status=400)


class BoardSingleView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    serializer_class = BoardSerializer
    queryset = Board.objects.all()


# List all the pins from a board
class BoardPinsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, rq, pk):
        try:
            board = Board.objects.get(pk=pk)
            board_pins = board.pins.all()

            pin_ser = PinSerializer(board_pins, many=True)
            return Response(pin_ser.data, status=200)

        except Exception as e:
            return Response({"error": "No board found"}, status=400)



#  add pin to board

class AddPinToBoardView(APIView):
    def post(self,rq,pinid,boardid):
        # return Response("ok",status=200)
        try:
            board = Board.objects.get(pk=boardid)
            pin = Pin.objects.get(pk=pinid)

            board.pins.add(pin)

            return Response({"msg":"added"},status=200)

        except:
            return Response({"error":"Pin / Board is not correct"},status=400)

