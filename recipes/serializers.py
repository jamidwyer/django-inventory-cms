from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'ingredients', 'instructions', 'estimated_cost']
