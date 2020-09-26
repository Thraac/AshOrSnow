from django.contrib import admin
from django.urls import path, include
from .views import weather_view, search_view

urlpatterns = [
    path('search', search_view),
    path('weather', weather_view),
]