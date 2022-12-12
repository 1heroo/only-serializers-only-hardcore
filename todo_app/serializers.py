from rest_framework import serializers

from todo_app.models import ToDoList, ToDoItem


class ToDoListDetailSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    def to_representation(self, instance):
        representation = super().to_representation(instance=instance)
        representation['items'] = instance.items.all().values_list()
        return representation


class ToDoListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    def create(self, validated_data):
        ToDoList.objects.create(**validated_data)
        return validated_data


class ItemSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=1000, required=False)
    due_date = serializers.DateField(required=False)
    todo_list = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        ToDoItem.objects.create(**validated_data)
        return validated_data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.save()
        return validated_data

