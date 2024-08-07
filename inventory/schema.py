import graphene
from graphene_django import DjangoObjectType
from django_filters import OrderingFilter
from .models import Product, InventoryItem
from core.models import User


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class InventoryItemType(DjangoObjectType):
    class Meta:
        model = InventoryItem


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    product = graphene.Field(ProductType, id=graphene.Int(),
                             name=graphene.String())

    products = graphene.List(ProductType)

    inventory_items = graphene.List(InventoryItemType)

    order_by = OrderingFilter(
               fields=(('expiration_date'),))

    viewer = graphene.Field(lambda: Query)

    def resolve_viewer(self, info):
        return self

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Product.objects.get(pk=id)

        if name is not None:
            return Product.objects.get(name=name)

        return None

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_inventory_items(self, info, **kwargs):
        return InventoryItem.objects.all()


schema = graphene.Schema(query=Query)
