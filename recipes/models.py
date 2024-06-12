from django.db.models import Model, CharField, ForeignKey, IntegerField, ManyToManyField, CASCADE
from core.models import User
from inventory.models import QuantitativeUnit, Product


class Ingredient(Model):
    quantity = IntegerField
    unit = ForeignKey(QuantitativeUnit, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)

    def __str__(self):
        return self.product.name


class Recipe(Model):
    instructions: CharField(max_length=500)
    name: CharField(max_length=500)
    person = ManyToManyField(User, blank=True, default='')
