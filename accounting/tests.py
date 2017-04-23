import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()

from importlib import import_module
from accounting.models import Transaction
from accounting.methods import get_transactions_by_date, get_sum, add_transaction, remove_transaction_by_id
from ajax_testing.models import RequestEntry
from django.test import TestCase
import pickle



class AccountingTest(TestCase):
    def test_collected_data(self):
        tests = RequestEntry.objects.filter(function_name__contains='accounting').order_by('-id').all()
        for t in tests:
            if 'get_transactions_by_date' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(list(get_transactions_by_date(*(inputs))), list(outputs))
                else:
                    with self.assertRaises(Exception):
                        get_transactions_by_date(*(pickle.loads(t.input_json)))

            elif 'get_sum' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(get_sum(*(inputs)), outputs)
                else:
                    with self.assertRaises(Exception):
                        get_sum(*(pickle.loads(t.input_json)))

            elif 'add_transaction' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(add_transaction(*(inputs)), outputs)
                else:
                    with self.assertRaises(Exception):
                        add_transaction(*(pickle.loads(t.input_json)))

            elif 'remove_transaction_by_id' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)

                    t = Transaction.objects.last()
                    id = t.id
                    t.id = inputs[0]
                    t.save()
                    self.assertEqual(remove_transaction_by_id(*(inputs)), outputs)
                    t.id = id
                    t.save()

                else:
                    with self.assertRaises(Exception):
                        remove_transaction_by_id(*(pickle.loads(t.input_json)))
            else:
                name = t.function_name
                inputs = pickle.loads(t.input_json)
                p, m = name.rsplit('.', 1)
                module = import_module(p)
                method = getattr(module, m)
                if t.success:
                    self.assertEqual(method(*inputs).content, pickle.loads(t.output_json).content)
                else:
                    with self.assertRaises(Exception):
                        method(*inputs)