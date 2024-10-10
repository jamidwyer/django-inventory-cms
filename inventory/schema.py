import graphene
from graphene import relay, Node
from graphene_django import DjangoObjectType
from django_filters import OrderingFilter
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from .models import Product, InventoryItem, QuantitativeUnit
from core.models import User
from graphql_jwt.decorators import login_required

class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class UnitType(DjangoObjectType):
    class Meta:
        model = QuantitativeUnit


class InventoryItemType(DjangoObjectType):
    class Meta:
        model = InventoryItem
        fields = ('id', 'product', 'expiration_date', 'person', 'quantity', 'unit')
        filter_fields = {'product__name': ['icontains'], 'person__id': ['exact']}
        interfaces = (Node, )
        interfaces = (graphene.Node,)


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    product = graphene.Field(ProductType, id=graphene.Int(),
                             name=graphene.String())

    products = graphene.List(ProductType)

    units = graphene.List(UnitType)

#    inventory_items = graphene.List(InventoryItemType)
    inventory_items = DjangoFilterConnectionField(InventoryItemType)

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
        return Product.objects.all().order_by('name')

    def resolve_units(self, info, **kwargs):
        return QuantitativeUnit.objects.all().order_by('name')

    @login_required
    def resolve_inventory_items(self, info, **kwargs):
        user = info.context.user
        return InventoryItem.objects.filter(person=user).order_by('expiration_date')


class UpdateItemQuantity(relay.ClientIDMutation):
    success = graphene.Boolean()
    message = graphene.String()
    inventory_item = graphene.Field(lambda: InventoryItemType) 

    class Input:
        id = graphene.String(required=True)
        quantity = graphene.Int(required=True)

    def mutate_and_get_payload(cls, info, id, quantity, **kwargs):
        try:
            item_id = from_global_id(id)[1]

            inventory_item = InventoryItem.objects.get(id=item_id)
            inventory_item.quantity = quantity
            inventory_item.save()

            return UpdateItemQuantity(success=True, inventory_item=inventory_item)
        except InventoryItem.DoesNotExist:
            return UpdateItemQuantity(success=False, message="Item not found.")
        except Exception as e:
            return UpdateItemQuantity(success=False, message=f"An error occurred: {str(e)}")


class QuantitativeUnitInput(graphene.InputObjectType):
    id = graphene.Int(required=True)


class InventoryItemInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    quantity = graphene.Int(required=True)
    unit_id = graphene.Int(required=False)
    expiration_date = graphene.String(required=True)


class CreateInventoryItem(graphene.Mutation):
    inventory_item = graphene.Field(InventoryItemType)

    class Arguments:
        new_inventory_item = InventoryItemInput(required=True)

    def mutate(self, info, new_inventory_item):
        user = info.context.user

        if user.is_anonymous:
            raise Exception("Authentication credentials were not provided.")

        user_id = user.id
        
        # TODO: inventory item needs to have person
        inventory_item = InventoryItem.objects.create(product_id=new_inventory_item.id, person_id=user_id, quantity=new_inventory_item.quantity, expiration_date=new_inventory_item.expiration_date, unit_id=new_inventory_item.unit_id)
        return CreateInventoryItem(inventory_item=inventory_item)


class DeleteInventoryItem(relay.ClientIDMutation):
    success = graphene.Boolean()
    message = graphene.String()

    class Input:
        id = graphene.ID(required=True)

    item = graphene.Field(InventoryItemType)

    def mutate_and_get_payload(cls, info, id):
        try:
            item_id = from_global_id(id)[1]

            item = InventoryItem.objects.get(id=item_id)
            item.delete()
            return DeleteInventoryItem(success=True, message="Item deleted successfully.")
        except InventoryItem.DoesNotExist:
            return DeleteInventoryItem(success=False, message="Item not found.")
        except Exception as e:
            return DeleteInventoryItem(success=False, message=f"An error occurred: {str(e)}")


class Mutation(graphene.ObjectType):
    create_inventory_item = CreateInventoryItem.Field()
    update_item_quantity = UpdateItemQuantity.Field()
    delete_inventory_item = DeleteInventoryItem.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
