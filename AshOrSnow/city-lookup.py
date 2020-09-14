from django.http import HttpResponse
import requests
import AshOrSnow.testContent

# constants
api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y'



# need to take input
# search = input("Please enter the city you want to")
search = 'denver'

# need input to be searched with city finder API

# city_url = (f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={search}") # location search
# city_response = requests.get(city_url) # location search response 
# city_id = bytes.decode(city_response.content).split(",") # loction id from response
# city_split = city_id

print(city_split[1])
# need to take results and find just the city number
# need to take city number and search weather api with it
# need to return information for weather for that city
