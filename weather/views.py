from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Weather



def weather_view(request, *args, **kwargs):
    temp = Weather.city_temperature
    return render(request, "home.html", status = 200)
