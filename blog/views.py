from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import Post, Category
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import PostSerializer, CommentSerializer


class PostAPIView(APIView):

    def get(self, request):
        blogs = Post.objects.all()
        return Response(blogs.values_list(), status=status.HTTP_200_OK)


class CategoryAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        return Response(categories.values_list(), status=status.HTTP_200_OK)


class PostDetailAPIView(APIView):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentAPIView(APIView):

    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

