from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
# Create your views here.


def reserve_table(request):

    reservation_form = ReservationForm()

    return render(request, "reservation.html", {
        "reservation_form": reservation_form,
    })
