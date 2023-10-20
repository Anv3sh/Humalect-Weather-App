from django.db import models
import uuid
from django.contrib.sessions.models import Session
# Create your models here.
class City(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    name = models.CharField(max_length=255, null=False, unique= True)
    data = models.JSONField(null=False)
    forecast_data = models.JSONField(null=False, default=None)
    class Meta:
        db_table = "city"


class CustomSession(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, primary_key=True)
    cities = models.ManyToManyField(City)

    class Meta:
        db_table = "customsessions"
    