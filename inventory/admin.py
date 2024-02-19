from django.contrib import admin

# Register your models here.
from .models import InventoryItem, Product, QuantitativeUnit

admin.site.register(InventoryItem)
admin.site.register(Product)
admin.site.register(QuantitativeUnit)
