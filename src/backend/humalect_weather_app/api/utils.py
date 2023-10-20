import os
import requests
from database.models import City, CustomSession
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

api_key = os.getenv("ACCUWEATHER_API_KEY")
base_url = os.getenv("ACCUWEATHER_BASE_URL")

def get_city_key(city_name):

    endpoint = f'/locations/v1/cities/search'
    
    try:
        # Make request to AccuWeather API to get city details
        response = requests.get(f'{base_url}{endpoint}', params={'q': city_name, 'apikey': api_key})
        if response.status_code == 200:
            city_details = response.json()
            if city_details:
                city_key = city_details[0]['Key']
                return city_key
            
    except Exception as e:
        raise e

def get_autocomplete(city_name):
    endpoint = f'/locations/v1/cities/autocomplete'
    try:
        # Make request to AccuWeather API to get city details
        response = requests.get(f'{base_url}{endpoint}', params={'apikey': api_key,'q': city_name})
        if response.status_code == 200:
            cities = response.json()
            city = cities[0]
            return city
    except Exception as e:
        return e
    
def get_weather_by_city(city_name):
    endpoint = f'/locations/v1/cities/search'
    
    try:
        # Make request to AccuWeather API to get city details
        response = requests.get(f'{base_url}{endpoint}', params={'q': city_name, 'apikey': api_key})
        if response.status_code == 200:
            city_details = response.json()
            if city_details:
                city_key = city_details[0]['Key']
                city_name = city_details[0]['EnglishName']
                # Get weather data for the city
                endpoint = f'/currentconditions/v1/{city_key}'
                weather_response = requests.get(f'{base_url}{endpoint}', params={'apikey': api_key,'details':"true"})
                
                if weather_response.status_code == 200:
                    weather_data = weather_response.json()[0]
                    return {
                        "city_key":city_key,
                        "city_name":city_name,
                        "weather_data":weather_data,
                        "forecast_data":get_forecast(city_key)
                    }
            return None
    except Exception as e:
        raise e

def get_forecast(city_key):
    endpoint = f'/forecasts/v1/hourly/12hour/{city_key}'
    try:
        response = requests.get(f'{base_url}{endpoint}', params={'apikey': api_key,'metric':'true'})
    except Exception as e:
        raise e
    if response.status_code == 200:
        forecast_data = response.json()
        return forecast_data
    return None
    

def get_current_custom_session(request):
    print(request.session.session_key)
    session = Session.objects.get(session_key = request.session.session_key)
    try:
        custom_session = CustomSession.objects.get(session=session)
    except CustomSession.DoesNotExist:
        custom_session = CustomSession(session=session)
        custom_session.save()
    return custom_session

def add_city_to_current_session(request,city):
    try:
        current_session = get_current_custom_session(request)
        if not current_session.cities.filter(name=city.name).exists():
            current_session.cities.add(city)
    except Exception as e:
        raise e
    
def get_cities_of_current_session(request):
    custom_session = get_current_custom_session(request)
    return custom_session.cities.all()

