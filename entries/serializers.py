from rest_framework import serializers

from entries.models import Entry


class EntrySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=1000)
    date_created = serializers.DateTimeField(read_only=True, required=False)

    def create(self, validated_data):
        Entry.objects.create(**validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
