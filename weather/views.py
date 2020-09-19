from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def weather_view(request, *args, **kwargs):

    return render(request, "home.html", status = 200)
