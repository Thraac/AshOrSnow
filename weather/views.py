from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Weather, City
from .forms import HomeForm



def weather_view(request, *args, **kwargs):
    form = HomeForm()
    search = input()
    return render(request=request,
                template_name="home.html",
                context={"weather": City.objects.all, "form": form}, 
                status = 200)
