import graphene
from graphene_django import DjangoObjectType
from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    mymodels = graphene.List(ProductType)

    def resolve_mymodels(self, info, **kwargs):
        return Product.objects.all()


schema = graphene.Schema(query=Query)
