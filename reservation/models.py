from django.db import models


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Reservation by {self.name}"
