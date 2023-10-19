import requests
from humalect_weather_app.settings import RAPIDAPI_KEY
from database.models import City, CustomSession
from django.contrib.sessions.models import Session

def get_weather_by_city(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":city}

    headers = {
	"X-RapidAPI-Key": RAPIDAPI_KEY,
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def get_current_custom_session(request):
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

