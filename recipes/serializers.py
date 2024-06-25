from rest_framework import serializers

from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'cook_time', 'prep_time', 'estimated_cost',
                  'url']
        read_only_fields = ['id']