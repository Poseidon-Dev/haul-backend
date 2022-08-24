"""
Serializers for the Equipment API View
"""
from rest_framework import serializers

from .models import Transfers

class TransfersSerializer(serializers.ModelSerializer):
    """Serializer for the equipment object """
    company_name = serializers.PrimaryKeyRelatedField(source='to_company.short_name', read_only=True)
    division_name = serializers.PrimaryKeyRelatedField(source='to_division.name', read_only=True)
    description = serializers.PrimaryKeyRelatedField(source='equipment_id.description_1', read_only=True)
    
    class Meta:
        model = Transfers
        fields = [
        'equipment_id',
        'to_company',
        'to_division',
        'to_status',
        'ask_date',
        'accepted_date',
        'completed_date',
        'completed',
        'description', 
        'company_name', 
        'division_name',
        ]
        read_only_fields = ['description', 'company_name', 'division_name',]

    def create(self, validated_data):
        print(validated_data)
        return Transfers.objects.create(**validated_data)
   
class TransfersDetailSerialzer(TransfersSerializer):

    class Meta(TransfersSerializer.Meta):
        fields = TransfersSerializer.Meta.fields