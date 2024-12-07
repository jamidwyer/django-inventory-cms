from django.contrib import admin
from django.shortcuts import redirect
from .models import InventoryItem, Product, QuantitativeUnit

admin.site.register(QuantitativeUnit)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("product", "expiration_date", "quantity", "unit", "person")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        if "_save" in request.POST:
            return redirect('/')
        elif "_addanother" in request.POST:
            return super().response_add(request, obj, post_url_continue)
        elif "_continue" in request.POST:
            return super().response_add(request, obj, post_url_continue)
        else:
            return super().response_add(request, obj, post_url_continue)
