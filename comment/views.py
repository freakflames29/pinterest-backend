from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import  CommentSerializer
from rest_framework import generics
from  .models import Comment

class CommentListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes =  [JWTAuthentication]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()



