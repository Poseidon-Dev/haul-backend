"""
Serializers for the Equipment API View
"""
from rest_framework import serializers

from .models import Company, Division

class CompanySerializer(serializers.ModelSerializer):
    """Serializer for the equipment object """
    
    class Meta:
        model = Company
        fields = ['company_id', 'name', 'short_name']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

class DivisionSerializer(serializers.ModelSerializer):
    """Serializer for the equipment object """
    
    class Meta:
        model = Division
        fields = ['company_id', 'division_id', 'name', 'short_name']

    def create(self, validated_data):
        return Division.objects.create(**validated_data)


