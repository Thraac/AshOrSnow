from django.db import models

# Create your models here.
class City(models.Model):
    lookup_city = models.CharField(max_length=100)

    def __str__(self):
        return self.lookup_city

class Weather(models.Model):
    weather_type = models.CharField(max_length=50)
    weather_image = models.CharField(max_length=3)
    city_temperature = models.CharField(max_length=4)

    def __str__(self):
        return self.weather_type, self.weather_image, self.city_temperature
