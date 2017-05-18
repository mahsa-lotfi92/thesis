import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()

from library.views import add_book, filter_by_date, filter_by_name
from django.test import TestCase
from django.test import RequestFactory


class LibraryNadiaTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_urls(self):
        request = self.factory.get('/library/add_book', {'date':'2017/02/10', 'price': '100000', 'name': 'test',
                                                         'author': 'test', 'desc': 'test book', 'available': 5})
        response = add_book(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/library/filter_by_date', {'start': '2017/02/9', 'end': '2017/02/9'})
        response = filter_by_date(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get('/accounting/filter_by_name', {'name': 'tes'})
        response = filter_by_name(request)
        self.assertEqual(response.status_code, 200)
