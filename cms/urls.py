from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)
from graphene_django.views import GraphQLView

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cms.schema import schema
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie

router = routers.DefaultRouter()


urlpatterns = [
    # TODO: csrf non-exempt
    path('graphql', csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True,
                                                     schema=schema)))),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
    path('', include(router.urls)),
    path('api/recipes/', include('recipes.urls')),
    path('api/inventory/', include('inventory.urls')),
]

admin.site.site_header = 'Hord CMS'
admin.site.site_title = 'Hord CMS'
