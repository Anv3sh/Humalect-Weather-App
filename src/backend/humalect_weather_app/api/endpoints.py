from django.urls import path
from api.views import health, get_weather

urlpatterns = [
    path("",health, name= "home"),
    path("weather/<str:city>", get_weather, name="get_weather")
]