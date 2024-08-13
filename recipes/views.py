from rest_framework import viewsets
from recipes.models import Recipe
from recipes import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        if product_id is not None:
            Recipe.objects.filter(ingredient__id=product_id).order_by('name')
        return Recipe.objects.all().order_by('name')
