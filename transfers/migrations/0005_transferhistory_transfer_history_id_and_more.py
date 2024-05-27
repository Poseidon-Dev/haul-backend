# Generated by Django 4.1 on 2022-09-01 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0005_equipment_status_alter_equipment_company_id_and_more"),
        ("transfers", "0004_transferhistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="transferhistory",
            name="transfer_history_id",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="transferhistory",
            name="equipment_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING, to="equipment.equipment"
            ),
        ),
    ]