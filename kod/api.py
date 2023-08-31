from rest_framework import viewsets, permissions

from . import serializers
from . import models


class KODViewSet(viewsets.ModelViewSet):
    """ViewSet for the KOD class"""

    queryset = models.KOD.objects.all()
    serializer_class = serializers.KODSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Status class"""

    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
