import graphene
from graphene_django import DjangoObjectType
from django_filters import OrderingFilter
from .models import Product, InventoryItem


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class InventoryItemType(DjangoObjectType):
    class Meta:
        model = InventoryItem


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)

    inventoryItems = graphene.List(InventoryItemType)

    order_by = OrderingFilter(
               fields=(('expiration_date'),))

    class Arguments:
        user_id = graphene.ID()

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_inventory_items(self, info, user_id, **kwargs):
        return InventoryItem.objects.get(user_id=user_id)


schema = graphene.Schema(query=Query)
