# Generated by Django 4.2.13 on 2024-07-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(),
        ),
    ]
