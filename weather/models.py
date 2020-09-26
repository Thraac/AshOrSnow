from django.db import models

# Create your models here.

class Weather(models.Model):

    city_weather = models.CharField(max_length=50, default='')
    city_weather_image = models.CharField(max_length=3, default='')
    city_temperature = models.CharField(max_length=4, default='')
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.weather_type, self.weather_image, self.city_temperature, self.city
