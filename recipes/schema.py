import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Recipe, Ingredient
from django.core.exceptions import ObjectDoesNotExist


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = "__all__"
        filter_fields = {'name': ['icontains'], 'ingredient__product__id': ['exact']}
        interfaces = (Node, )

    recipe_id = graphene.ID()

    def resolve_recipe_id(self, info):
        return self.id


class Query(graphene.ObjectType):
    recipe = graphene.Field(RecipeType, id=graphene.ID(required=True),
                            name=graphene.String())

    recipes = DjangoFilterConnectionField(RecipeType)

    class Arguments:
        ingredient_id = graphene.ID(required=True)

    def resolve_recipe(self, info, id: graphene.ID = None, name: str = None):
        try:
            if id:
                return Recipe.objects.get(pk=id)

            if name:
                return Recipe.objects.get(name=name)

        except ObjectDoesNotExist:
            return None

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()


schema = graphene.Schema(query=Query)
