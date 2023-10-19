import requests
from humalect_weather_app.settings import RAPIDAPI_KEY

def get_weather_by_city(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":city}

    headers = {
	"X-RapidAPI-Key": RAPIDAPI_KEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()