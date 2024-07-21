import graphene

import inventory.schema as inventory_app
import recipes.schema as recipes_app

class Query(inventory_app.schema.Query, recipes_app.schema.Query, graphene.ObjectType):
    # Inherits all classes and methods from app-specific queries, so no need
    # to include additional code here.
    pass

schema = graphene.Schema(query=Query)
