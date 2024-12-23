from django.shortcuts import render
from .serializers import  CommentSerializer
from rest_framework import generics
from  .models import Comment

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()



