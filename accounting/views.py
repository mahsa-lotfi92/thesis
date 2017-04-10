from datetime import datetime
from django.http.response import HttpResponse

from accounting.methods import add_transaction


def add_income(request):
    date = datetime.strptime(request.GET['date'])
    amount = request.GET('amount')
    add_transaction(date, amount, True)
    return HttpResponse(status=200)


def add_outgoing(request):
    date = datetime.strptime(request.GET['date'])
    amount = request.GET('amount')
    add_transaction(date, amount)
    return HttpResponse(status=200)

