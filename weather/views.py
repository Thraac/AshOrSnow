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

    city_proper = str(city).title()

    return render(request, 
                'results.html', 
                {'city': city_proper, 'weather': weather, 
                'temperature': temperature, 'weather_icon': weather_icon})


# if you are trying to use this code and it does not work you might need your own api key (limited to 50 searches a day)
def search(request, *args, **kwargs):
    api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y' 

    try:
        # grabs the city that was input 
        input_city = request.POST.get('city')
        city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={input_city}") 
        city_response = requests.get(city_url).json()[0]["Key"] # saves the response from api for city ID

    except:
        # Set up the search again and lets them know they did not have a search
        #  (KeyError, CityLookup.DoesNotExist)
        return render(request, 'home.html', {
            'error_message': "The city you submitted was not found. Please try again.",
        })

    else:
        # this section of code is where the look up of weather information occurs

        weather_url = (f"http://dataservice.accuweather.com/currentconditions/v1/{city_response}?apikey={api_key}") # uses the city response and the api key to grab weather information
        weather_response = requests.get(weather_url) # saves the response from api for weather details
        weather_icon_number = int(weather_response.json()[0]['WeatherIcon']) # saves the number for the weather icon and converts it to int for following code
        if weather_icon_number<10: # this makes sure that if the icon number is below 10 it will change the number
            weather_icon_number = str(weather_icon_number).zfill(2) # this adds a zero infront of the icon number because it needs to be 01 no 1 or it will fail
            
        temperature = weather_response.json()[0]['Temperature']['Imperial']['Value'] # this is the temperature
        weather_type = weather_response.json()[0]['WeatherText'] # this is the type of weather right now


        weather_icon = (f"https://developer.accuweather.com/sites/default/files/{weather_icon_number}-s.png") # saves the url for the weather icon
        # weather look up ends here

        # This is where data is being saved to the database for each module
        # saving the input to the city
        new_city = CityLookup(city = input_city)
        new_city.save()

        new_weather = Weather(city = new_city, weather = weather_type) 
        new_weather.save()

        new_temperature = Temperature(city = new_city, temperature = temperature)
        new_temperature.save()

        new_weather_icon = WeatherIcon(city = new_city, weather_icon = weather_icon)
        new_weather_icon.save()

        # Redirects to the results page since data is being posted
        test = new_city.id
        return HttpResponseRedirect(reverse('weather:results', args=(test,)))

