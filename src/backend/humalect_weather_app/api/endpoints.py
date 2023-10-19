from django.urls import path
from api.views import home, get_weather

urlpatterns = [
    path("",home, name= "home"),
    path("weather/<str:city_name>", get_weather, name="get_weather")
]