from rest_framework import viewsets
from recipes.models import Recipe
from recipes import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all().order_by('name')

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = self.queryset.filter(person__id=user_id)
        return queryset
