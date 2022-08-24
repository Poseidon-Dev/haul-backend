"""
Views for the equipment API
"""
import csv
from rest_framework import viewsets

from .models import Equipment
from profiles.models import Company, Division
from equipment import serializers

class ActiveEquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EquipmentDetailSerialzer
    queryset = Equipment.objects.filter(status=0)

    def create_dummy_data(self):
        Equipment._send_dummy_data(self)
        with open('C:/dev/00 - Projects/00-Apps/haul-back/dummy_data.csv', newline='') as fin:
            heading = next(fin)
            reader = csv.reader(fin, delimiter=',')
            payload = {}
            for row in reader:
                payload['company_id'] = Company.objects.filter(company_id=int(row[0])).first()
                
                if int(row[8]) >= 0 and int(row[8]) < 10:
                    payload['division_id'] = Division.objects.filter(division_id=0).first()
                elif int(row[8]) >= 10 and int(row[8]) < 20:
                    payload['division_id'] = Division.objects.filter(division_id=1).first()
                elif int(row[8]) >= 20 and int(row[8]) < 30:
                    payload['division_id'] = Division.objects.filter(division_id=2).first()
                elif int(row[8]) >= 30 and int(row[8]) < 40:
                    payload['division_id'] = Division.objects.filter(division_id=3).first()
                elif int(row[8]) >= 40 and int(row[8]) < 50:
                    payload['division_id'] = Division.objects.filter(division_id=4).first()
                elif int(row[8]) >= 50 and int(row[8]) < 60:
                    payload['division_id'] = Division.objects.filter(division_id=5).first()
                elif int(row[8]) >= 60 and int(row[8]) < 70:
                    payload['division_id'] = Division.objects.filter(division_id=6).first()
                elif int(row[8]) >= 70 and int(row[8]) < 80:
                    payload['division_id'] = Division.objects.filter(division_id=7).first()
                elif int(row[8]) >= 80 and int(row[8]) < 90:
                    payload['division_id'] = Division.objects.filter(division_id=8).first()
                elif int(row[8]) >= 90 and int(row[8]) < 100:
                    payload['division_id'] = Division.objects.filter(division_id=9).first()
                elif int(row[8]) >= 100 and int(row[8]) < 110:
                    payload['division_id'] = Division.objects.filter(division_id=10).first()
                elif int(row[8]) >= 110 and int(row[8]) < 120:
                    payload['division_id'] = Division.objects.filter(division_id=11).first()
                elif int(row[8]) >= 120 and int(row[8]) < 130:
                    payload['division_id'] = Division.objects.filter(division_id=12).first()
                else:
                    payload['division_id'] = 0

                payload['equipment_id'] = row[1]
                payload['description_1'] = row[2]
                payload['description2'] = row[3]
                payload['description3'] = row[4]
                payload['serial'] = row[5]
                payload['model'] = row[6]
                payload['model_year'] = row[12]
                payload['status_code'] = row[7]
                payload['department'] = row[8]
                payload['item_class'] = row[9]
                payload['job_number'] = row[10]
                payload['warehouse'] = row[11]

                e = Equipment.objects.create(**payload)
                e.save()

    def get_queryset(self):
        return self.queryset.filter(division_id=3)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EquipmentSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()


class TransferEquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EquipmentDetailSerialzer
    queryset = Equipment.objects.filter(status=1)

    def get_queryset(self):
        return self.queryset.filter(division_id=3)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EquipmentSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()
