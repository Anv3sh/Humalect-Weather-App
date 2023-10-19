import requests
from humalect_weather_app.settings import RAPIDAPI_KEY

def get_weather_by_city(city):
    url = f'https://community-open-weather-map.p.rapidapi.com/weather?q={city}&units=metric'
    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': 'community-open-weather-map.p.rapidapi.com'
    }

    response = requests.get(url, headers=headers)
    return response.json()