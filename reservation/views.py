from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Reservation


def reserve_table(request):
    return HttpResponse("Hello, page!")
