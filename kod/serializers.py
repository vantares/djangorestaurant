from rest_framework import serializers

from . import models


class KODSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KOD
        fields = [
            "last_updated",
            "created",
            "staff_id",
            "kod_nemu_item",
            "kod_status",
        ]

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status
        fields = [
            "created",
            "last_updated",
            "status",
        ]
