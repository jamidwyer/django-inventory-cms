from django.test import SimpleTestCase, TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command


class TestView(TestCase):

    def test_get_recipes(self):
        client = APIClient()
        res = client.get('/inventoryItems/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, ["Black Beans"])


@patch('inventory.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
