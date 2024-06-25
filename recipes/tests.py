from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from core.models import User
from recipes.models import Recipe


class TestView(TestCase):

    def test_get_recipes(self):
        client = APIClient()
        res = client.get('/recipes/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, ["Beans and Rice"])


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
