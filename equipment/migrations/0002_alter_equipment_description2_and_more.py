# Generated by Django 4.1 on 2022-08-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='description2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description 2'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description 3'),
        ),
    ]
