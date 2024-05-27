from django.db import models

from equipment.models import Equipment

class Location(models.Model):
    equipment_id = models.OneToOneField(
        Equipment,
        on_delete=models.CASCADE,
        default=1,
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        )
    speed = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        )
    heading = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        )
    
