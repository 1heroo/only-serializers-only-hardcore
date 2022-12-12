from django.shortcuts import render

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EntrySerializer
from entries.models import Entry


class EntryListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        entries = Entry.objects.all()
        return Response(entries.values_list(), status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EntrySerializer)
    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EntryDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Entry.objects.get(pk=pk)

    def get(self, request, pk):
        serializer = EntrySerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EntrySerializer)
    def patch(self, request, pk):
        instance = self.get_object(pk=pk)
        serializer = EntrySerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.get_object(pk=pk).delete()
        return Response(status.HTTP_204_NO_CONTENT)
