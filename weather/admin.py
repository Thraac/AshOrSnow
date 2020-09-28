from django.contrib import admin

# Register your models here.
from .models import CityLookup, Weather, Temperature, WeatherIcon

admin.site.register(CityLookup)
admin.site.register(Weather)
admin.site.register(Temperature)
admin.site.register(WeatherIcon)