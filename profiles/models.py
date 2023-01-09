from django.db import models


class Company(models.Model):
    company_id = models.IntegerField(
        primary_key=True,
        unique=True
    )
    name = models.CharField(
        max_length=255
    )
    short_name = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.company_id}: {self.name}'


class Division(models.Model):
    company_id = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        default=1
    )
    division_id = models.IntegerField(
        primary_key=True,
        unique=True
    )
    name = models.CharField(
        max_length=255
    )
    short_name = models.CharField(
        max_length=5,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.division_id}: {self.name}'

