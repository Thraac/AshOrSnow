from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests, json

from .models import CityLookup, Weather, Temperature, WeatherIcon


def home(request):
    city_list = CityLookup.objects.all()
    context = {'city_list': city_list}
    return render(request, 'home.html', context)



def results(request, city_id):
    city = get_object_or_404(CityLookup, pk=city_id)
    weather = get_object_or_404(Weather, pk=city_id)
    temperature = get_object_or_404(Temperature, pk=city_id)
    weather_icon = get_object_or_404(WeatherIcon, pk=city_id)
    return render(request, 'results.html', {'city': city, 'weather': weather, 'temperature': temperature, 'weather_icon': weather_icon})

def search(request, *args, **kwargs):
    # city = get_object_or_404(CityLookup, pk=city_id)
    api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y'

    try:
        input_city = request.POST.get('city')
    except (KeyError, Weather.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'home.html', {
            'city': city,
            'error_message': "You didn't submit a city.",
        })
    else:
        new_city = CityLookup(city = input_city)
        new_city.save()

        # this section of code is where the look up of weather information occurs
        city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={input_city}") 
        city_response = requests.get(city_url).json()[0]["Key"]

        weather_url = (f"http://dataservice.accuweather.com/currentconditions/v1/{city_response}?apikey={api_key}") # uses the city response and the api key to grab weather information
        weather_response = requests.get(weather_url)
        weather_icon_number = weather_response.json()[0]['WeatherIcon']

        temperature = weather_response.json()[0]['Temperature']['Imperial']['Value'] # this is the temperature
        weather_type = weather_response.json()[0]['WeatherText'] # this is the type of weather right now
        weather_icon = (f"https://developer.accuweather.com/sites/default/files/{weather_icon_number}-s.png")
        # weather look up ends here
        new_weather = Weather(city = new_city, weather = weather_type)
        new_weather.save()

        new_temperature = Temperature(city = new_city, temperature = temperature)
        new_temperature.save()

        new_weather_icon = WeatherIcon(city = new_city, weather_icon = weather_icon)
        new_weather_icon.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        test = new_city.id
        return HttpResponseRedirect(reverse('weather:results', args=(test,)))

