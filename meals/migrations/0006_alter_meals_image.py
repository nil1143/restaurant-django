# Generated by Django 4.2.13 on 2024-07-22 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0005_alter_meals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(upload_to='assets'),
        ),
    ]
