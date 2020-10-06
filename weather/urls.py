from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.home, name='home'),                              
    path('search/', views.search, name='search'),
]