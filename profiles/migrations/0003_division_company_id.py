# Generated by Django 4.1 on 2022-08-23 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_company_short_name_division_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='company_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.company'),
        ),
    ]