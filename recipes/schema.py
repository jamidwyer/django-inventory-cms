import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = "__all__"
        filter_fields = ('name', )
        interfaces = (Node, )
        interfaces = (graphene.Node,)


class Query(graphene.ObjectType):
    recipes = DjangoFilterConnectionField(RecipeType)

    class Arguments:
        ingredient_id = graphene.ID()

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()


schema = graphene.Schema(query=Query)
