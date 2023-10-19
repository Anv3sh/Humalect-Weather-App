from django.urls import path
from api.endpoints import health, home, get_weather

urlpatterns = [
    path("",home, name= "home"),
    path("health/",health, name="health"),
    path("weather/<str:city_name>", get_weather, name="get_weather")
]