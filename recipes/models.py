from django.conf import settings
from django.db.models import (Model, CharField, ForeignKey, IntegerField,
                              TextField, DecimalField,  ManyToManyField,
                              CASCADE)
from inventory.models import QuantitativeUnit, Product


class Tag(Model):
    value = CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.value


class Ingredient(Model):
    quantity = IntegerField
    unit = ForeignKey(QuantitativeUnit, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)

    def __str__(self):
        return self.product.name


class Recipe(Model):
    instructions = TextField(blank=True)
    ingredients = ManyToManyField(
        'Ingredient',
        related_name='recipes'
    )
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
 #   tag = ForeignKey(Tag, related_name='recipes', on_delete=CASCADE,
                    #  blank=True, null=True)

    def __str__(self):
        return self.name
