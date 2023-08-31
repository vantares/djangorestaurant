from rest_framework import viewsets, permissions

from . import serializers
from . import models


class KOTMenuItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the KOTMenuItem class"""

    queryset = models.KOTMenuItem.objects.all()
    serializer_class = serializers.KOTMenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class KOTStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the KOTStatus class"""

    queryset = models.KOTStatus.objects.all()
    serializer_class = serializers.KOTStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class KOTViewSet(viewsets.ModelViewSet):
    """ViewSet for the KOT class"""

    queryset = models.KOT.objects.all()
    serializer_class = serializers.KOTSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderChannelViewSet(viewsets.ModelViewSet):
    """ViewSet for the OrderChannel class"""

    queryset = models.OrderChannel.objects.all()
    serializer_class = serializers.OrderChannelSerializer
    permission_classes = [permissions.IsAuthenticated]
