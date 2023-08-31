from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "description",
            "last_updated",
            "name",
            "created",
        ]

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = [
            "created",
            "last_updated",
            "item_category",
        ]
