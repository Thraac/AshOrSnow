from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.home, name='home'),                              #home page
    path('<int:city_id>/results/', views.results, name='results'),  #search results page
    path('search/', views.search, name='search'),
]