from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

def get_foster_collector():
    return get_user_model().objects.get_or_create(username='taneleer-tivan')[0]

class Collection(models.Model):
    display_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    creator = models.CharField(max_length=200, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET(get_foster_collector))
    homepage = models.URLField()
    icon = models.ImageField(upload_to='collection_icons', height_field=100, width_field=100)
    history = HistoricalRecords()

class Collectible(models.Model):
    pass

class Universum(models.Model):
    display_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    creator = models.CharField(max_length=200, default='')
    homepage = models.URLField()
    icon = models.ImageField(upload_to='universum_icons', height_field=100, width_field=100)

    def __str__(self) -> str:
        return self.display_name