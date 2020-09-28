from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:city_id>/', views.detail, name='detail'),
    path('<int:city_id>/results/', views.results, name='results'),
    path('<int:city_id>/vote/', views.vote, name='vote'),
]