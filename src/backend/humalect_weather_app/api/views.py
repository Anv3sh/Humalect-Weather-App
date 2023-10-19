import requests
from django.http.response import JsonResponse , HttpResponseServerError
from humalect_weather_app.settings import RAPIDAPI_KEY
from api.utils import get_weather_by_city

def health(request):
    return JsonResponse({"message":"Welcome to the weather app."})

def get_weather(request,city):
    try:
        weather_data = get_weather_by_city(city)
        return JsonResponse({"data":weather_data})
    
    except Exception as e:
        return HttpResponseServerError("Internal Server Error:", str(e))

