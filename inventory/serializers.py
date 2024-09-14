from rest_framework import serializers
from inventory.models import InventoryItem, Product, QuantitativeUnit


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
        )


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantitativeUnit
        fields = (
            'id',
            'name',
        )


class InventoryItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    unit = UnitSerializer(many=False, read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'product', 'quantity', 'expiration_date', 'unit']
