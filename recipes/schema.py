import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Recipe, Ingredient


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = "__all__"
        filter_fields = {'name': ['icontains'], 'ingredient__product__id': ['exact']}
        interfaces = (Node, )
        interfaces = (graphene.Node,)


class Query(graphene.ObjectType):
    recipe = graphene.Field(RecipeType, id=graphene.Int(),
                            name=graphene.String())

    recipes = DjangoFilterConnectionField(RecipeType)

    class Arguments:
        ingredient_id = graphene.ID()

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Recipe.objects.get(pk=id)

        if name is not None:
            return Recipe.objects.get(name=name)

        return None

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()


schema = graphene.Schema(query=Query)
