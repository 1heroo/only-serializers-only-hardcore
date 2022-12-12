from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from pycasts.models import Episode


class PodcastSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    pub_date = serializers.DateTimeField()
    link = serializers.URLField()
    image = serializers.URLField()
    podcast_name = serializers.CharField(max_length=100)
    guid = serializers.CharField(max_length=500)


class PodcastsAPIView(APIView):

    def get(self, request):
        episodes = Episode.objects.filter().order_by("-pub_date")[:10]
        serializer = PodcastSerializer(episodes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)