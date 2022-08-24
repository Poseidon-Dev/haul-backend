"""
Serializers for the Equipment API View
"""
from rest_framework import serializers

from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    """Serializer for the equipment object """

    company_name = serializers.CharField(source='company_id.short_name')
    division_name = serializers.CharField(source='division_id.name')
    
    class Meta:
        model = Equipment
        fields = [
        'company_id',
        'company_name',
        'division_id',
        'division_name',
        'equipment_id',
        'description_1',
        'description2',
        'description3',
        'serial',
        'model',
        'model_year',
        'status_code',
        'department',
        'item_class',
        'job_number',
        'warehouse',
        'status',
        ]

    def create(self, validated_data):
        return Equipment.objects.create(**validated_data)
   
class EquipmentDetailSerialzer(EquipmentSerializer):

    class Meta(EquipmentSerializer.Meta):
        fields = EquipmentSerializer.Meta.fields