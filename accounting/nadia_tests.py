import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()

from accounting.models import Transaction
from django.test import TestCase
from accounting.views import list_transactions, add_income, add_outgoing, filter_by_date, remove_transaction
from django.test import RequestFactory


class LibraryNadiaTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_urls(self):
        # request = self.factory.get('/accounting/')
        # response = list_transactions(request)
        # self.assertEqual(response.status_code, 200)

        request = self.factory.get('/accounting/add_income_transaction', {'date':'2017/02/10', 'amount': '100000'})
        response = add_income(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/accounting/add_outgoing_transaction', {'date': '2017/02/10', 'amount': '10000'})
        response = add_outgoing(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/accounting/filter_by_date', {'start': '2017/02/9', 'end': '2017/02/9'})
        response = filter_by_date(request)
        self.assertEqual(response.status_code, 200)


        request = self.factory.get('/accounting/remove_transaction/2')
        response = remove_transaction(request, 2)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/accounting/remove_transaction/80000000')
        response = remove_transaction(request, 800000)
        self.assertEqual(response.status_code, 500)

        # with self.assertRaises(Exception):
        #     method(*inputs)


