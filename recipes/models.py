from django.conf import settings
from django.db.models import (Model, CharField, ForeignKey, IntegerField,
                              TextField, DecimalField,  ManyToManyField,
                              CASCADE)
from inventory.models import QuantitativeUnit, Product


class Recipe(Model):
    instructions = TextField(blank=True)
    ingredients = ManyToManyField(Product, through='Ingredient')
    name = CharField(max_length=255)
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        null=True,
    )
    cook_time = IntegerField(blank=True, null=True)
    prep_time = IntegerField(blank=True, null=True)
    estimated_cost = DecimalField(max_digits=5, decimal_places=2, blank=True,
                                  null=True)
    url = CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Ingredient(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    recipe = ForeignKey(Recipe, on_delete=CASCADE, blank=True, null=True)
    quantity = CharField(max_length=100, blank=True, null=True) 
    unit = ForeignKey(QuantitativeUnit, on_delete=CASCADE) 
    
    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.product.name}"

