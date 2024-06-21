from .models import Reservation
from django import forms

# from django.forms import ModelForm, TextInput, EmailInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("name", "email", "phone", "number_of_persons", "date", "time")

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Email",
                }
            ),
            "phone": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Phone",
                }
            ),
            "number_of_persons": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Number of persons",
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Date",
                }
            ),
            "time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Time",
                }
            ),
        }
