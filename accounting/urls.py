from django.conf.urls import url
from django.shortcuts import render

from accounting.views import add_income
from ajax_testing.dynamic_import import run_method
from ajax_testing.views import request_week

urlpatterns = [
    url(r'^$', lambda r: render(r, 'home.html')),
    url(r'add_income_transaction$', add_income),
    url(r'add_outgoing_transaction$', add_outgoing),
    url(r'run_methods$', run_method),
]
