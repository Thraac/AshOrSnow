from django.contrib import admin
from django.urls import path, include
from .views import HomeView, WeatherView

app_name = 'weather'
urlpatterns = [
    path('home', HomeView.as_view(), name='search'),
    path('weather', WeatherView.as_view(), name='weather'),
]