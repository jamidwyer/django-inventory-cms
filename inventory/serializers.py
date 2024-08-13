from rest_framework import serializers
from inventory.models import InventoryItem


class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.SlugRelatedField(many=False, read_only=True,
                                           slug_field='name')

    class Meta:
        model = InventoryItem
        fields = ['id', 'product', 'quantity', 'expiration_date']
