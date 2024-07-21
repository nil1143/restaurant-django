from . import views
from django.urls import path


urlpatterns = [
        path('', views.meal_list , name='meals')

]