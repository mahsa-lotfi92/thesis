from django.test import TestCase
import json
# Create your tests here.
from ajax_testing.views import get_week


class GetWeekTest(TestCase):
    def test_collected_data(self):
        tests = open('tests.txt').readlines()
        for t in tests:
            input_json, output_json = t.split(' ')[0], t.split(' ')[1]
            if output_json:
                print(111111, output_json)
                self.assertEqual(get_week(*(json.loads(input_json))), json.loads(output_json))
            else:
                self.assertRaises(Exception, get_week(*(json.loads(input_json))))