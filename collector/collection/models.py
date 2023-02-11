from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from polymorphic.models import PolymorphicModel
from simple_history.models import HistoricalRecords

# Create your models here.

def get_foster_collector():
    return get_user_model().objects.get_or_create(username='taneleer-tivan')[0]

def get_foster_creator():
    return CreatorPerson.objects.get_or_create(nickname='The omnipotent')[0]

class Creator(PolymorphicModel):
    slug = models.CharField(max_length=200, unique=True)

class CreatorPerson(Creator):
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    nickname = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        name = ''
        if len(self.first_name) != 0:
            name = self.first_name
        if len(self.middle_name) != 0:
            if len(name) != 0:
                name = f'{name} {self.middle_name}'
            else:
                name = self.middle_name
        if len(self.last_name) != 0:
            if len(name) != 0:
                name = f'{name} {self.last_name}'
            else:
                name = self.last_name
        if len(self.nickname) != 0:
            if len(name) != 0:
                name = f'{name} ({self.nickname})'
            else:
                name = f'({self.middle_name})'
        return name  

class CreatorCompany(Creator):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Universum(models.Model):
    display_name = models.CharField(max_length=200, unique=True)
    short_name = models.CharField(max_length=10)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    creator = models.ForeignKey(
        Creator,
        on_delete=models.SET(get_foster_creator),
        related_name='universums'
    )
    homepage = models.URLField()
    icon = models.ImageField(
        upload_to='universum_icons',
        height_field='icon_height',
        width_field='icon_width')
    icon_height = models.PositiveSmallIntegerField(default=15)
    icon_width = models.PositiveSmallIntegerField(default=15)

    def __str__(self) -> str:
        return self.display_name

class UniversumCategory(models.Model):
    display_name = models.CharField(max_length=200, unique=True)
    universum = models.ForeignKey(
        Universum,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    def __str__(self) -> str:
        return f'{self.display_name} ({self.universum.short_name})'

class UniversumType(models.Model):
    display_name = models.CharField(max_length=200, unique=True)
    universum = models.ForeignKey(
        Universum,
        on_delete=models.CASCADE,
        related_name='types'
    )

    def __str__(self) -> str:
        return f'{self.display_name} ({self.universum.short_name})'

class Collection(models.Model):
    display_name = models.CharField(max_length=200, default='Collection')
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_foster_collector),
        related_name='collections',
        default=get_foster_collector
    )
    homepage = models.URLField()
    icon = models.ImageField(
        upload_to='collection_icons',
        height_field='icon_height',
        width_field='icon_width'
    )
    icon_height = models.PositiveSmallIntegerField(default=15)
    icon_width = models.PositiveSmallIntegerField(default=15)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.display_name

class Collectible(models.Model):
    display_name = models.CharField(max_length=200, default='Collectible')
    slug = models.CharField(max_length=200, unique=True)
    unique = models.BooleanField(default=False)
    description = models.TextField(default='')
    creator = models.ForeignKey(
        Creator,
        on_delete=models.SET(get_foster_creator),
        related_name='collectibles',
        default=get_foster_creator
    )
    collections = models.ManyToManyField(
        Collection,
        related_name='collectibles',
        related_query_name='collectible'
    )
    categories = models.ManyToManyField(
        UniversumCategory,
        related_name='collectibles',
        related_query_name='collectible'
    )
    types = models.ManyToManyField(
        UniversumType,
        related_name='collectibles',
        related_query_name='collectible'
    )
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.display_name