from rest_framework import serializers

from . import models


class KOTMenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KOTMenuItem
        fields = [
            "last_updated",
            "quantity",
            "created",
            "menu_item",
            "kot",
        ]

class KOTStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KOTStatus
        fields = [
            "status",
            "last_updated",
            "created",
        ]

class KOTSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KOT
        fields = [
            "last_updated",
            "staff_id",
            "out_time",
            "created",
            "in_time",
            "status",
            "order_channel",
        ]

class OrderChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderChannel
        fields = [
            "name",
            "created",
            "last_updated",
            "close_time",
            "open_time",
            "description",
        ]
