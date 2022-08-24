"""
Views for the equipment API
"""
from rest_framework import viewsets

from .models import Transfers
from transfers import serializers

class TransfersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransfersDetailSerialzer
    queryset = Transfers.objects.filter(ask_date__isnull=False, accepted_date__isnull=True, completed_date__isnull=True)

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TransfersSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()

class ScheduledTransfersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransfersDetailSerialzer
    queryset = Transfers.objects.filter(ask_date__isnull=False, accepted_date__isnull=False, completed_date__isnull=True)

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TransfersSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()

class HistoryTransfersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransfersDetailSerialzer
    queryset = Transfers.objects.filter(ask_date__isnull=False, accepted_date__isnull=False, completed_date__isnull=False)

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TransfersSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()

