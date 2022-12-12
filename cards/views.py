from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cards.models import Card
from cards.serializers import CardSerializer


# Create your views here.

class CardAPIView(APIView):

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CardSerializer)
    def post(self, request):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CardDetailAPIView(APIView):

    @swagger_auto_schema(request_body=CardSerializer)
    def patch(self, request, pk):
        card = Card.objects.get(pk=pk)
        serializer = CardSerializer(instance=card, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class BoxAPIView(APIView):

    def get(self, request, box_id):
        if box_id not in range(1, 6):
            return Response('No boxes found', status=status.HTTP_404_NOT_FOUND)

        cards = Card.objects.filter(box=box_id)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)