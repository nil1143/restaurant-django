from django.db import models

# Create your models here.
class Meals(models.Model):
    class MealType(models.TextChoices):
        STARTER = "Starter"
        MAIN_COURSE = "Main Course"
        DESSERT = "Dessert"

    name = models.CharField(max_length=60)
    description = models.TextField(max_length=300)
    meal_type = models.CharField(null=True, max_length= 20, choices=MealType.choices)
    image = models.ImageField(upload_to="static/assets/")