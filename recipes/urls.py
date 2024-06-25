from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipes import views

router = DefaultRouter
router.register(prefix='recipes', viewset=views.RecipeViewSet, basename='recipes')

app_name = 'recipes'

urlpatterns = [
    path('', include(router.urls)),
]
