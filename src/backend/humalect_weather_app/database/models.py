from django.db import models
import uuid
from django.contrib.sessions.models import Session
# Create your models here.
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, null=False)
    data = models.JSONField(null=False)

    class Meta:
        db_table = "city"


class CustomSession(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, primary_key=True)
    city = models.ForeignKey(City, on_delete= models.DO_NOTHING )

    class Meta:
        db_table = "customsessions"
    