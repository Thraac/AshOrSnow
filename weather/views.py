from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import CityLookup, Weather, Temperature, WeatherIcon


def index(request):
    city_list = CityLookup.objects.all()
    context = {'city_list': city_list}
    return render(request, 'index.html', context)

def detail(request, city_id):
    city = get_object_or_404(CityLookup, pk=city_id)
    return render(request, 'detail.html', {'city': city})

def results(request, city_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % city_id)

def vote(request, city_id):
    city = get_object_or_404(CityLookup, pk=city_id)

    try:
        input_city = city.weather_set.get(pk=request.POST['city'])
    except (KeyError, Weather.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'city': city,
            'error_message': "You didn't submit a city.",
        })
    else:
        Weather.city = input_city
        Weather.save(city)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('weather:results', args=(city.id,)))

    return HttpResponse("You're voting on question %s." % city_id)