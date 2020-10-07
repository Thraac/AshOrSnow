from django.test import TestCase
import requests


class TestWeather(TestCase):
    """
    Test makes sure that URLs are set up right when requesting information
    """
    def test_location_response(self):
        location = 'Denver'
        api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y' 
        response = requests.get((f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={location}")) 
        self.assertEqual(response.status_code, 200)

    def test_weather_response(self):
        location_key = '347810'
        api_key = 'LXGGpNcbto33jbyFGv0yBADrLm8KEu8y' 
        response = requests.get((f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}")) 
        self.assertEqual(response.status_code, 200)