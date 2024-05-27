import os
import re
import requests
from .models import GPSUnit
from core import config as c

class GPSTrackITEndpoint:
    BASE_URL = c.GPSTRACKIT_PROD_ENDPOINT
    API_KEY = c.GPSTRACKIT_API_KEY
    endpoint = ''
    def __init__(self):
        self.headers = {
            'x-api-key': self.API_KEY,
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            }
        self.base_uri = self.BASE_URL + self.endpoint


class UnitEndpoint(GPSTrackITEndpoint):
    model = GPSUnit
    endpoint = 'units/'

    def __init__(self, params=None):
        self.params = params
        super(UnitEndpoint, self).__init__()

    def _fetch_all(self):
        r = requests.get(self.base_uri, headers=self.headers, params=self.params)
        return r.json()

    def _fetch_one(self, device_id):
        r = requests.get(self.base_uri + str(device_id), headers=self.headers, params=self.params)
        return r.json()

    def all(self, device_id=None):
        print(device_id)
        if device_id:
            dataset = self._fetch_one(device_id)
            print(dataset)
        else:
            dataset = self._fetch_all()
        return [
            GPSUnit(
                account_id=data.get('accountId'),
                device_id=data.get('deviceId'),
                unit_id=data.get('unitId'),
                device_label=self.clean_device_label(data.get('deviceLabel')),
                driver_id=data.get('driverId'),
                engine_hours=data.get('engineHours'),
                engine_odometer=data.get('engineOdometer'),
                last_message_time=data.get('LastMessageTime'),
                make=data.get('make'),
                model=data.get('model'),
                year=data.get('year'),
                vin=data.get('vin'),
                latitude=data.get('latitude'),
                longitude=data.get('longitute'),
                unit_time=data.get('unitTime'),
            )
            for data in dataset ]
    @staticmethod
    def clean_device_label(device_label):
        if device_label:
            device_label = str.strip(device_label)
            device_label = device_label[:5]
            return device_label
        else:
            return None