from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Meals

# Create your views here.


class MealList(generic.ListView):
    queryset = Meals.objects.all()
    template_name = "meals.html"
