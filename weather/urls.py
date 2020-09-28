from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:city_id>/results/', views.results, name='results'),
    path('search/', views.search, name='search'),
]