from django.http import HttpResponse
import requests
import json

# constants
api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y'
search = 'denver' # for test
city_response = '347810' # for test

def weatherLookup():
    # need to take input
    # search = input("Please enter the city you want to search: ").lower()

    # need input to be searched with city finder API
    city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={search}") # location search

    # need to take results and find just the city number
    city_response = requests.get(city_url).json()[0]["Key"] # location search response with just the city ID

    # need to take city number and search weather api with it
    weather_url = (f"http://dataservice.accuweather.com/currentconditions/v1/{city_response}?apikey={api_key}") # uses the city response and the api key to grab weather information
    weather_response = requests.get(weather_url)

    # need to return information for weather for that city
    temperature = weather_response.json()[0]['Temperature']['Imperial']['Value'] # this is the temperature
    weather_type = weather_response.json()[0]['WeatherText'] # this is the type of weather right now
    weather_icon_number = weather_response.json()[0]['WeatherIcon'] # this is an int32 image that displays accuweathers image for the current weather state
    weather_icon = (f"https://developer.accuweather.com/sites/default/files/{weather_icon_number}-s.png")


