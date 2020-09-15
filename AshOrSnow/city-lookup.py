from django.http import HttpResponse
import requests
import json
# import testContent

# constants
api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y'

# need to take input
# search = input("Please enter the city you want to").lower()
search = 'denver'

# need input to be searched with city finder API
city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={search}") # location search
city_response = requests.get(city_url) # location search response 
city_id = bytes.decode(city_response.content).split(",")[1].split(":")[1] # loction id from response

# need to take results and find just the city number
# need to take city number and search weather api with it

weather_url = (f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{city_id}?apikey={api_key}")
weather_response = requests.get(weather_url)

# need to return information for weather for that city
