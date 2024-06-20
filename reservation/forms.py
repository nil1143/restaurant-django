from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'number_of_persons', 'date', 'time')