from rest_framework import serializers
from inventory.models import InventoryItem, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
        )


class InventoryItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'product', 'quantity', 'expiration_date']
