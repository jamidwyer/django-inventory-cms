import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Recipe, Tag, Ingredient


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = "__all__"
        filter_fields = ('name', )
        interfaces = (Node, )
        interfaces = (graphene.Node,)


class Query(graphene.ObjectType):
    tag = graphene.Field(TagType, id=graphene.Int(), name=graphene.String())

    tags = graphene.List(TagType)

    recipe = graphene.Field(RecipeType, id=graphene.Int(),
                            name=graphene.String())

    recipes = DjangoFilterConnectionField(RecipeType)

    class Arguments:
        ingredient_id = graphene.ID()

    def resolve_tag(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Tag.objects.get(pk=id)

        if name is not None:
            return Tag.objects.get(name=name)

        return None

    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Recipe.objects.get(pk=id)

        if name is not None:
            return Recipe.objects.get(name=name)

        return None

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.select_related('tag').all()


schema = graphene.Schema(query=Query)
