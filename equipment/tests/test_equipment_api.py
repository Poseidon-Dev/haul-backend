from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from equipment.models import Equipment

CREATE_EQUIPMENT_URL = reverse('equipment:create')

def create_equipment(**params):
    return Equipment.objects.create(**params)

class PublicEquipmentApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_equipment_success(self):
        payload = {
            'equipment_id': '12345',
            'description_1': 'Test Description'
        }
        res = self.client.post(CREATE_EQUIPMENT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        equipment = Equipment.objects.get(equipment_id=payload['equipment_id'])
        self.assertTrue(equipment.equipment_id == '12345')

