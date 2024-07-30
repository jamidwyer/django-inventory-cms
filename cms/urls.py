from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)
from graphene_django.views import GraphQLView

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from inventory.models import InventoryItem
from recipes.models import Recipe
from cms.schema import schema
from django.views.decorators.csrf import csrf_exempt


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
        fields = ['id', 'ingredients']


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all().order_by('name')
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(person__id=user_id)
        return queryset


router = routers.DefaultRouter()


urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
    path('', include(router.urls)),
]
