from django.urls import include, path
from rest_framework import routers
from recipes import views


router = routers.DefaultRouter()

router.register('', views.RecipeViewSet, basename='recipes')

app_name = 'recipes'

urlpatterns = [
    path('', include(router.urls)),
]
