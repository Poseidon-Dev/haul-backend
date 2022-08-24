"""
Views for the profile API
"""
from rest_framework import viewsets

from .models import Company, Division
from profiles import serializers

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def perform_create(self, serializer):
        serializer.save()

class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DivisionSerializer
    queryset = Division.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def perform_create(self, serializer):
        serializer.save()

