from django.db import models

from profiles.models import Company, Division

class Equipment(models.Model):
    company_id = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE,
        default=1
    )
    division_id = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        default=0
    )
    equipment_id = models.CharField(
        verbose_name='Equipment ID',
        max_length=8,
        blank=False,
        null=False,
        primary_key=True,
        unique=True,
    )
    description_1 = models.CharField(
        verbose_name='Description',
        max_length=30,
        blank=False,
        null=False
    )
    description2 = models.CharField(
        verbose_name='Description 2',
        max_length=255,
        blank=True,
        null=True,
    )
    description3 = models.CharField(
        verbose_name='Description 3',
        max_length=255,
        blank=True,
        null=True,
    )
    serial = models.CharField(
        verbose_name='Serial',
        max_length=255,
    )
    model = models.CharField(
        verbose_name='Model',
        max_length=255,
    )
    model_year = models.IntegerField(
        verbose_name='Year',
    )
    status_code  = models.IntegerField(
        verbose_name='Status',
    )
    department = models.IntegerField(
        verbose_name='Department',
    )
    item_class = models.IntegerField(
        verbose_name='Class',
    )
    job_number = models.CharField(
        verbose_name='Job Number',
        max_length=255,
        blank=True,
        null=True,
    )
    warehouse = models.CharField(
        verbose_name='Warehouse',
        max_length=255,
    )
    status = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    trackit_id = models.IntegerField()

    @property
    def company(self):
        return self.company.name
        
    @property
    def division(self):
        return self.division.name

    def __str__(self):
        return f'{self.equipment_id}: {self.description_1}'
