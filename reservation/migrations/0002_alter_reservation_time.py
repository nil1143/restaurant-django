# Generated by Django 4.2.13 on 2024-07-05 01:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
