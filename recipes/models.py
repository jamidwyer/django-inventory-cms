from django.db.models import Model, CharField, ManyToManyField
from django.contrib.auth.models import User
from inventory.models import Ingredient


class Recipe(Model):
    ingredients = ManyToManyField(Ingredient)
    instructions: CharField(max_length=500, blank=True, default='')
    name: CharField(max_length=500, blank=True, default='')
    person = ManyToManyField(User, blank=True, default='')
