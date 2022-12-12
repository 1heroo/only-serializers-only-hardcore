from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

from .models import ToDoItem, ToDoList
from rest_framework.views import APIView

from .serializers import ToDoListSerializer, ToDoListDetailSerializer, ItemSerializer


class ListListAPIView(APIView):

    def get(self, request):
        lists = ToDoList.objects.all()
        return Response(lists.values_list(), status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ToDoListSerializer)
    def post(self, request):
        serializer = ToDoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListDetailAPIView(APIView):

    def get_object(self, pk):
        return ToDoList.objects.get(pk=pk)

    def get(self, request, pk):
        list = self.get_object(pk=pk)
        serializer = ToDoListDetailSerializer(list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListItemAPIView(APIView):

    @swagger_auto_schema(request_body=ItemSerializer)
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemDetailAPIView(APIView):

    def get_object(self, pk):
        return ToDoItem(pk=pk)

    @swagger_auto_schema(request_body=ItemSerializer)
    def patch(self, request, pk):
        item = self.get_object(pk=pk)
        serializer = ItemSerializer(instance=item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
