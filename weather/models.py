from django.db import models

class CityLookup(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Weather(models.Model):
    city = models.ForeignKey(CityLookup, on_delete=models.CASCADE)
    weather = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.weather

class WeatherIcon(models.Model):
    city = models.ForeignKey(CityLookup, on_delete=models.CASCADE)
    weather_icon = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.weather_icon


class Temperature(models.Model):
    city = models.ForeignKey(CityLookup, on_delete=models.CASCADE)
    temperature = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.temperature