from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Reservation
from .forms import ReservationForm

# Create your views here.


def reserve_table(request):

    if request.method == "POST":
        reservation_form = ReservationForm(data=request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Booking approved and waiting approval!!"
            )
    reservation_form = ReservationForm()

    return render(
        request,
        "reservation.html",
        {
            "reservation_form": reservation_form,
        },
    )


class ReservationList(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = "reservation_list.html"
