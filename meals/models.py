from django.db import models

# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=300)
    meal_type = models.TextChoices("Starter", "Main Course", "Dessert")
    image = models.ImageField(upload_to="static/assets/")