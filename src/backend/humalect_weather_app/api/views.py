import requests
import json
from uuid import uuid4
from django.http.response import JsonResponse , HttpResponseServerError
from humalect_weather_app.settings import RAPIDAPI_KEY
from api.utils import get_weather_by_city,add_city_to_current_session,get_cities_of_current_session

from database.models import City, CustomSession
from django.contrib.sessions.models import Session


def health(request):
    return JsonResponse({"message":"Welcome to the weather app."})

def home(request):
    cities = get_cities_of_current_session(request)
    cities_data = {}
    for city in cities:
        cities_data.update(
            {
                "name":city.name,
                "data":city.data
            }
        )
    return JsonResponse({"status":200,"body":{"cities_data":cities_data}})

def get_weather(request,city_name):
    try:
        city = City.objects.get(name=city_name)
        add_city_to_current_session(request,city)
        weather_data = city.data
        return JsonResponse(
            {
            "status":200,
            "body":{"data":weather_data}
            }
        )
    except City.DoesNotExist:
        weather_data = get_weather_by_city(city_name)
        city = City(name=city_name,data=weather_data)
        city.save()

        try:
            add_city_to_current_session(request,city)
        except Exception as e:
            return HttpResponseServerError("Internal server error!", str(e))

        return JsonResponse(
            {
                "status":201,
                "body":{"data":weather_data}
            }
        )

