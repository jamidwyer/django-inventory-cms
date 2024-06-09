from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from inventory.models import InventoryItem


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']


class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.StringRelatedField(many=False)

    class Meta:
        model = InventoryItem
        fields = ['id', 'quantity', 'product', 'expiration_date']


class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        queryset = InventoryItem.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(person__id=user_id)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'inventoryItems', InventoryItemViewSet, basename='InventoryItem')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
