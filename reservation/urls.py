from . import views
from django.urls import path


urlpatterns = [
    path('', views.reserve_table , name='reserve_table'),
]