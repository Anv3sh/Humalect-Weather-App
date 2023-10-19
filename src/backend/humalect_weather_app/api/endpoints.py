import requests
import json
from uuid import uuid4
from api.utils import (
    get_weather_by_city,
    add_city_to_current_session,
    get_cities_of_current_session,
    get_forecast,
    get_city_key
)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from database.models import City, CustomSession
from django.contrib.sessions.models import Session



@api_view(['GET'])
def health(request):
    return Response({"message":"Welcome to the weather app."})

@api_view(['GET'])
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
    return Response({"body":{"cities_data":cities_data}},status=200)

@api_view(['GET'])
def get_weather(request,city_name):
    try:
        city_key = get_city_key(city_name)
        print(city_key)
        city = City.objects.get(id=city_key)
        # add_city_to_current_session(request,city)
        weather_data = city.data
        return Response(
            {
            "body":{"data":weather_data,"forecast_data":get_forecast(city.id)}
            },
            status=200
        )
    except City.DoesNotExist:
        response = get_weather_by_city(city_name)
        print(response)
        if response:
            city = City(
                id=response["city_key"],
                name=response["city_name"],
                data=response["weather_data"]
            )
            city.save()

        # try:
        #     add_city_to_current_session(request,city)
        # except Exception as e:
        #     return HttpResponseServerError("Internal server error!", str(e))

            return Response(
                {
                    "body":{
                        "data":response["weather_data"],
                        "forecast_data":get_forecast(response["city_key"])
                    }
                },
                status=200
            )
        return Response(
            {
                "body":{"message":"City not found."}
            },
            status=404
        )
