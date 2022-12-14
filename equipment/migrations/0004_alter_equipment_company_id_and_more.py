# Generated by Django 4.1 on 2022-08-23 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_division_company_id'),
        ('equipment', '0003_alter_equipment_job_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.company'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='division_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.division'),
        ),
    ]
