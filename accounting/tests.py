import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()


from accounting.methods import get_transactions_by_date, get_sum, add_transaction
from ajax_testing.models import RequestEntry
from django.test import TestCase
import pickle



class AccountingTest(TestCase):
    def test_collected_data(self):
        tests = RequestEntry.objects.filter(function_name__contains='accounting').all()
        for t in tests:

            if 'get_transactions_by_date' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(list(get_transactions_by_date(*(inputs))), list(outputs))
                else:
                    with self.assertRaises(Exception):
                        get_transactions_by_date(*(pickle.loads(t.input_json)))

            if 'get_sum' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(get_sum(*(inputs)), outputs)
                else:
                    with self.assertRaises(Exception):
                        get_sum(*(pickle.loads(t.input_json)))

            if 'add_transaction' in t.function_name:
                if t.success:
                    inputs = pickle.loads(t.input_json)
                    outputs = pickle.loads(t.output_json)
                    self.assertEqual(add_transaction(*(inputs)), outputs)
                else:
                    with self.assertRaises(Exception):
                        add_transaction(*(pickle.loads(t.input_json)))