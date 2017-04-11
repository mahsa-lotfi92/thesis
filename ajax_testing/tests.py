import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()


from ajax_testing.models import RequestEntry
from ajax_testing.methods import get_week
from django.test import TestCase
import pickle



class GetWeekTest(TestCase):
    def test_collected_data(self):
        tests = RequestEntry.objects.filter(function_name__contains='ajax_testing').all()
        for t in tests:

            if t.success:
                self.assertEqual(get_week(*(pickle.loads(t.input_json))), pickle.loads(t.output_json))
            else:
                with self.assertRaises(Exception):
                    get_week(*(pickle.loads(t.input_json)))
