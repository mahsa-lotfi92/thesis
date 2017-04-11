from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response

from accounting.methods import add_transaction, get_transactions_by_date, get_sum
from accounting.models import Transaction


def add_income(request):
    add_transaction(request.GET['date'], request.GET['amount'], True)
    return render_to_response('accounting.html', {'transactions': Transaction.objects.all()})


def add_outgoing(request):
    date = request.GET['date']
    amount = request.GET['amount']
    add_transaction(date, amount)
    return render_to_response('accounting.html', {'transactions': Transaction.objects.all()})


def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'accounting.html', {'transactions':transactions})


def filter_by_date(request):
    start = request.GET['start']
    end = request.GET['end']
    transactions = get_transactions_by_date(start, end)
    get, paid = get_sum(transactions)
    return render_to_response('accounting.html', {'transactions': transactions, 'paid': paid, 'get':get, 'reminded':get-paid})
