from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Weather


def search_view(request, *args, **kwargs):

    return render(request=request,
                template_name="search.html",
                context={"weather": Weather.objects.all}, 
                status = 200)


def weather_view(request, *args, **kwargs):

    return render(request=request,
                template_name="results.html",
                context={"weather": Weather.objects.all}, 
                status = 200)
