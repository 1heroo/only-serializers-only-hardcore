from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    technology = serializers.CharField(max_length=20)
    image = serializers.ImageField()

