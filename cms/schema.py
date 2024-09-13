import graphene
import graphql_jwt
from graphene_django.types import DjangoObjectType
from core.models import User
import inventory.schema as inventory_app
import recipes.schema as recipes_app


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password', )

class UserInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    username = graphene.String(required=False)
    password = graphene.String(required=True)


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=False)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User.objects.create_user(username=username, password=password, email=email)
        return CreateUser(user=user)
    

class Query(inventory_app.schema.Query, recipes_app.schema.Query, graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user 

        if user.is_authenticated:
            return user
        else:
            return None

class Mutation(inventory_app.schema.Mutation, graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
