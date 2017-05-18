import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()

from library.models import Book
from importlib import import_module
from ajax_testing.models import RequestEntry
from django.test import TestCase
import pickle


class LibraryTest(TestCase):

    def test_collected_data(self):
        tests = RequestEntry.objects.filter(function_name__contains='library').order_by('-id').all()
        for t in tests:
            name = t.function_name
            inputs = pickle.loads(t.input_json)
            p, m = name.rsplit('.', 1)
            module = import_module(p)
            method = getattr(module, m)

            if 'get_available_books' in t.function_name or \
                            'get_books_by_name' in t.function_name or \
                            'get_books_by_date' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(list(method(*(inputs))), list(outputs))
                else:
                    with self.assertRaises(Exception):
                        method(*(pickle.loads(t.input_json)))

            elif 'add_new_book' in t.function_name:
                if t.success:
                    self.assertEqual(method(*inputs), pickle.loads(t.output_json))
                else:
                    with self.assertRaises(Exception):
                        method(*inputs)

            elif 'add_book' in t.function_name:
                if t.success:
                    self.assertEqual(method(*inputs).status_code, pickle.loads(t.output_json).status_code)
                else:
                    with self.assertRaises(Exception):
                        method(*inputs)

            elif 'buy_book_by_id' in t.function_name:
                if t.success:
                    if pickle.loads(t.output_json):
                        b = Book.objects.get(id=inputs[0])
                        b.available += 1
                        b.save()
                    self.assertEqual(method(*(inputs)), pickle.loads(t.output_json))

            elif 'remove_book_by_id' in t.function_name:
                b = Book.objects.last()
                id = b.id
                b.id = inputs[0]
                b.save()
                self.assertEqual(method(*(inputs)), pickle.loads(t.output_json))
                b.id = id
                b.save()

            elif 'buy_book' in t.function_name\
                    or 'remove_book' in t.function_name:
                continue

            else:
                if t.success:
                    self.assertEqual(method(*inputs).content, pickle.loads(t.output_json).content)
                else:
                    with self.assertRaises(Exception):
                        method(*inputs)