from django.contrib import admin

from collection import models

# Register your models here.
collection_models = [
    models.Collection,
    models.Collectible,
    models.Universum,
    models.UniversumCategory,
    models.UniversumType,
    models.CreatorPerson,
    models.CreatorCompany
]

admin.site.register(collection_models)