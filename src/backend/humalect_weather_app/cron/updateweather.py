import requests
from database.models import City
from api.utils import get_weather_by_city, get_forecast

def update_weather():
    cities = City.objects.all()
    print("hello")
    print(cities)
    for city in cities:
        city.data = get_weather_by_city(city.name)["weather_data"]
        city.forecast_data = get_forecast(city.id)
        city.save()
