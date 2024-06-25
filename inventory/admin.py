from django.contrib import admin
from .models import InventoryItem, Product, QuantitativeUnit

admin.site.register(InventoryItem)
admin.site.register(Product)
admin.site.register(QuantitativeUnit)
