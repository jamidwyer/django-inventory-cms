from rest_framework import viewsets
from inventory.models import InventoryItem
from inventory import serializers


class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InventoryItemSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            return InventoryItem.objects.filter(person__id=user_id).order_by('expiration_date')
        return InventoryItem.objects.all().order_by('expiration_date')
