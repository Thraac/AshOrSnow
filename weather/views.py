from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

import json, requests

from .models import Weather


class HomeView(generic.ListView):
    template_name = 'search.html'
    model = Weather


class WeatherView(generic.ListView):
    model = Weather
    template_name = 'results.html'

    def run_query(self):
        # api key
        api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y'
        search = self.request.GET.get('city')
        

        # initial city search to get the city id
        city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={search}") # city search
        city_response = requests.get(city_url).json()[0]["Key"] # city response

        # weather search with city id 
        weather_url = (f"http://dataservice.accuweather.com/currentconditions/v1/{city_response}?apikey={api_key}") # weather search
        weather_response = requests.get(weather_url) # weather response
        
        # weather response data
        temperature = weather_response.json()[0]['Temperature']['Imperial']['Value'] # this is the temperature
        weather_type = weather_response.json()[0]['WeatherText'] # this is the type of weather right now
        weather_icon_number = weather_response.json()[0]['WeatherIcon'] # id for weather icon
        weather_icon = (f"https://developer.accuweather.com/sites/default/files/{weather_icon_number}-s.png") # weather icon

        results = {'temperature': temperature, 'weather': weather_type, 'icon': weather_icon}
        return results














# new views are being tested these are the old views

# def search_view(request, city_id, *args, **kwargs):
#     template_name="search.html"
#     city_searched = get_object_or_404(city, pk=city_id)

#     if request.method=='POST':
#         pass

#     return render(request=request,
#                 template_name="search.html",
#                 context={"weather": Weather.objects.all}, 
#                 status = 200)


# def weather_view(request, *args, **kwargs):

#     return render(request=request,
#                 template_name="results.html",
#                 context={"weather": Weather.objects.all}, 
#                 status = 200)
