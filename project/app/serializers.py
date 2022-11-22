from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField()

    def create(self, data):
        return Image.objects.create(**data)

    def update(self, instance, validated_data):
        print(instance)
        instance.image = validated_data["image"]
        instance.save()
        return instance
