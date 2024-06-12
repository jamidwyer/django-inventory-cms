from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from inventory.models import InventoryItem
from recipes.models import Recipe


class InventoryItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.StringRelatedField(many=False)

    class Meta:
        model = InventoryItem
        fields = ['id', 'quantity', 'product', 'expiration_date']


class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer

    def get_queryset(self):
        queryset = InventoryItem.objects.all().order_by('expiration_date')
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(person__id=user_id)
        return queryset


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'ingredients', 'instructions', 'name']


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all().order_by('name')
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(person__id=user_id)
        return queryset


router = routers.DefaultRouter()
router.register(r'inventoryItems', InventoryItemViewSet,
                basename='InventoryItem')
router.register(r'recipes', RecipeViewSet, basename='Recipe')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
