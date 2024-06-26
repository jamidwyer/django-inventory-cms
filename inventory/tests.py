from django.test import TestCase
from rest_framework.test import APIClient


class TestView(TestCase):

    def test_get_recipes(self):
        client = APIClient()
        res = client.get('/inventoryItems/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, ["Black Beans"])
