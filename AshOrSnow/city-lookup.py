from django.http import HttpResponse
import requests
import json
# import testContent

# constants
api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y'

# need to take input
# search = input("Please enter the city you want to").lower()
search = 'denver' # for test
city_response = '347810' # for test
# need input to be searched with city finder API

#the two city constants need to be unfrozen
# city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={search}") # location search
# city_response = requests.get(city_url).json()[0]["Key"] # location search response with just the city ID

# need to take results and find just the city number
# need to take city number and search weather api with it

# unfreeze the three below when done testing
weather_url = (f"http://dataservice.accuweather.com/currentconditions/v1/{city_response}?apikey={api_key}")
weather_response = requests.get(weather_url)
# print(weather_response.content)
temperature = weather_response.json()[0]['Temperature']['Imperial']['Value']
weather_type = weather_response.json()[0]['WeatherText']


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(weather_response.json())
print(temperature)
print(weather_type)
# need to return information for weather for that city
