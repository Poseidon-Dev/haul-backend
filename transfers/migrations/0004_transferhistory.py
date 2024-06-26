# Generated by Django 4.1 on 2022-09-01 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0005_equipment_status_alter_equipment_company_id_and_more"),
        ("profiles", "0003_division_company_id"),
        ("transfers", "0003_alter_transfers_equipment_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransferHistory",
            fields=[
                (
                    "equipment_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="equipment.equipment",
                    ),
                ),
                ("to_status", models.IntegerField(blank=True, null=True)),
                ("ask_date", models.DateTimeField(blank=True, null=True)),
                ("accepted_date", models.DateTimeField(blank=True, null=True)),
                ("completed_date", models.DateTimeField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
                (
                    "to_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.company",
                    ),
                ),
                (
                    "to_division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.division",
                    ),
                ),
            ],
        ),
    ]
