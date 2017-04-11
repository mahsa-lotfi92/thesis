from django.conf.urls import url
from django.shortcuts import render

from accounting.views import add_income, add_outgoing, list_transactions, filter_by_date

urlpatterns = [
    url(r'^$', list_transactions),
    url(r'add_income_transaction$', add_income),
    url(r'add_outgoing_transaction$', add_outgoing),
    url(r'filter_by_date$', filter_by_date),
]
