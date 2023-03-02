from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CommentSerializier
from rest_framework.response import Response
from .models import Comment
from rest_framework import viewsets
# Create your views here.
class PostCommentAPIView(APIView):
    def get(self, _, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializier(comments,many=True)
        return Response(serializer.data)

class CommentAPIView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializier(comment, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
# class PostViewset(viewsets.ModelViewSet):
#     serializer_class = PostSerializier
#     queryset = Post.objects.all()