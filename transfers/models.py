from django.db import models
from django.utils import timezone

from profiles.models import Company, Division
from equipment.models import Equipment

class Transfers(models.Model):
    equipment_id = models.OneToOneField(
        Equipment,
        on_delete=models.DO_NOTHING,
        primary_key=True,
    )
    from_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='transfers_from_company',
    )
    from_division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='transfers_from_division',
    )
    from_status = models.IntegerField(
        blank=True,
        null=True,
    )
    to_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='transfers_to_company',
    )
    to_division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='transfers_to_division',
    )
    to_status = models.IntegerField(
        blank=True,
        null=True,
    )
    ask_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    accepted_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    def __str__(self):
        return f'{self.equipment_id}: {self.equipment_id.description}'

    def save(self, *args, **kwargs):
        self.ask_date = timezone.now()
        return super(Transfers, self).save(*args, **kwargs)


class TransferHistory(models.Model):
    transfer_history_id = models.AutoField(
        primary_key=True
        )
    equipment_id = models.OneToOneField(
        Equipment,
        on_delete=models.DO_NOTHING,
        primary_key=False,
    )
    from_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='transfer_history_from_company',
    )
    from_division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='transfer_history_from_division',
    )
    from_status = models.IntegerField(
        blank=True,
        null=True,
    )
    to_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='transfer_history_to_company',
    )
    to_division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='transfer_history_to_division',
    )
    to_status = models.IntegerField(
        blank=True,
        null=True,
    )
    ask_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    accepted_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    completed = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    def __str__(self):
        return f'{self.equipment_id}: {self.equipment_id.description}'

    def save(self, *args, **kwargs):
        self.ask_date = timezone.now()
        return super(Transfers, self).save(*args, **kwargs)