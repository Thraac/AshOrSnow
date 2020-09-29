from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests, json

from .models import CityLookup, Weather, Temperature, WeatherIcon


def home(request):
    """
    View for the base home page
    """
    return render(request, 'home.html', context)



def results(request, city_id):
    """
    View for displaying weather information for searched city
    Pulls all information from the city modules related to the city
    """
    city = get_object_or_404(CityLookup, pk=city_id)
    weather = get_object_or_404(Weather, pk=city_id)
    temperature = get_object_or_404(Temperature, pk=city_id)
    weather_icon = get_object_or_404(WeatherIcon, pk=city_id)

    city_proper = str(city).title()

    return render(request, 
                'results.html', 
                {'city': city_proper, 'weather': weather, 
                'temperature': temperature, 'weather_icon': weather_icon})



def search(request, *args, **kwargs):
    """
    If you are trying to use this code and it does not work you might need your own api key (limited to 50 searches a day)
    This grabs the information input in the search bar and grabs it from the Accuweather Api
    If the search was not spelled correctly or the code limit has been reached it will display the error in except
    Everything under else is taking the data from acuweather and asigning it to the proper module
    Finally the view pulls up the ID of the searched city and redirects to display the results
    """
    
    api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y' 

    try:
        # grabs the city that was input 
        input_city = request.POST.get('city')
        city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={input_city}") 
        city_response = requests.get(city_url).json()[0]["Key"]

    except:
        # Sets up the search again if the code errors for any reason
        return render(request, 'home.html', {
            'error_message': "The city you submitted was not found. Please try again.",
        })

    else:
        # this section of code is where the look up of weather information occurs
        weather_url = (f"http://dataservice.accuweather.com/currentconditions/v1/{city_response}?apikey={api_key}") 
        weather_response = requests.get(weather_url) 
        weather_icon_number = int(weather_response.json()[0]['WeatherIcon']) 

        # the icon url requires 01 and api returns 1 this adds a 0 before the number if less than 10
        if weather_icon_number<10: 
            weather_icon_number = str(weather_icon_number).zfill(2) 
            
        temperature = weather_response.json()[0]['Temperature']['Imperial']['Value']
        weather_type = weather_response.json()[0]['WeatherText'] 
        weather_icon = (f"https://developer.accuweather.com/sites/default/files/{weather_icon_number}-s.png") 

        # Saving searches to database
        new_city = CityLookup(city = input_city)
        new_city.save()

        new_weather = Weather(city = new_city, weather = weather_type) 
        new_weather.save()

        new_temperature = Temperature(city = new_city, temperature = temperature)
        new_temperature.save()

        new_weather_icon = WeatherIcon(city = new_city, weather_icon = weather_icon)
        new_weather_icon.save()

        # Redirects to the results page since data is being posted
        new_city_id = new_city.id
        return HttpResponseRedirect(reverse('weather:results', args=(new_city_id,)))

