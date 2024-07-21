import graphene
from graphene_django import DjangoObjectType
from .models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe


class Query(graphene.ObjectType):
    mymodels = graphene.List(RecipeType)

    def resolve_mymodels(self, info, **kwargs):
        return Recipe.objects.all()


schema = graphene.Schema(query=Query)
