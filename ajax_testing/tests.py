import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")
django.setup()


from ajax_testing.methods import get_week
from django.test import TestCase
import json



class GetWeekTest(TestCase):
    def test_collected_data(self):
        tests = open('tests.txt').readlines()
        for t in tests:
            t.replace('\n', '')
            input_json= t.split()[0]
            output_json = None
            if len(t.split()) > 1:
                output_json = t.split()[1]
            if output_json:
                self.assertEqual(get_week(*(json.loads(input_json))), json.loads(output_json))
            else:
                with self.assertRaises(Exception):
                    get_week(*(json.loads(input_json)))
