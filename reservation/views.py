from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages

# Create your views here.


def reserve_table(request):

    reservation_form = ReservationForm()

    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
            '''
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking succesful!",
            )'''
    return render(
        request,
        "reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )
