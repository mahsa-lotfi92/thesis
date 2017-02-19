from django.http.response import HttpResponse
import re
from datetime import datetime

from ajax_testing.decorators import save_request


@save_request
def get_week(date):
    pattern = '(?P<year>\d{4})\/(?P<month>\d{2})\/(?P<day>\d{2})'
    res = re.match(pattern, date)
    date = datetime(day=int(res.group('day')), month=int(res.group('month')), year=int(res.group('year')))
    return (str(date.weekday()+2 % 7))


def request_week(request):
    return HttpResponse(get_week(request.GET['date']))