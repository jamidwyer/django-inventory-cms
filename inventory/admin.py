from django.contrib import admin
from .models import InventoryItem, Product, QuantitativeUnit

admin.site.register(Product)
admin.site.register(QuantitativeUnit)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("product", "expiration_date", "quantity", "unit", "person")