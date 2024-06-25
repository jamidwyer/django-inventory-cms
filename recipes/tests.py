from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from recipes.models import Recipe

from rest_framework import status
from rest_framework.test import APIClient

from recipes.serializers import RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    defaults = {
        'name': "Test Rec",
        'prep_time': 5,
        'cook_time': 20,
        'estimated_cost': 30.00,
        'instructions': 'Mix. Cook.',
        'link': 'hord.tech',
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipesAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipesAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpassw123'
        )
        self.client.force_authenticate(self.user)

    def test_get_recipes(self):
        create_recipe(user=self.user)
        create_recipe(user=self.user)
        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('name')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_recipes_by_user(self):
        other_user = get_user_model().objects.create_user(
            'other@example.com',
            'password123',
        )
        create_recipe(user=self.user)
        create_recipe(user=other_user)
        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class TestModels(TestCase):
    def test_create_recipes(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'test123'
        )

        recipe = Recipe.objects.create(
            user=user,
            name="Delicious food",
            prep_time=5,
            cook_time=5,
            estimated_cost=Decimal('20.10'),
            instructions='Mix. Cook.'
        )

        self.assertEqual(str(recipe), recipe.name)
