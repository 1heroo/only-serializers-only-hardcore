from rest_framework import serializers
from .models import Card

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class CardSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=100)
    answer = serializers.CharField(max_length=100)
    box = serializers.IntegerField(
        # choices=zip(BOXES, BOXES),
        # default=BOXES[0],
    )
    date_created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        Card.objects.create(**validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.box = validated_data.get('box', instance.box)
        instance.save()
        return validated_data
