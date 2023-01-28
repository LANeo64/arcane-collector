from django.db import models

# Create your models here.
class Collection(models.Model):
    display_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    creator = models.CharField(max_length=200, default='')
    homepage = models.URLField()
    icon = models.ImageField(upload_to='universum_icons', height_field=100, width_field=100)

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