from . import views
from django.urls import path


urlpatterns = [
    path('', views.reserve_table , name='reserve_table'),
    path('reservation-list', views.ReservationList.as_view(), name='reservation-list')
]