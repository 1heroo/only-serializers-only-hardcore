import datetime

from rest_framework import serializers

from blog.models import Comment, Post


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=1000)
    created_on = serializers.DateField(default=datetime.date.today, required=False)
    last_modified = serializers.DateField(default=datetime.date.today, required=False)
    categories = CategorySerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['comments'] = instance.comments.all().values_list()
        return representation


class CommentSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=1000)
    created_on = serializers.DateTimeField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    def create(self, validated_data):
        Comment.objects.create(**validated_data)
        return validated_data
