from django.http.response import HttpResponse

from ajax_testing.methods import get_week


def request_week(request):
    return HttpResponse(get_week(request.GET['date']))