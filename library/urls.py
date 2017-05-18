from django.conf.urls import url
from django.shortcuts import render

from library.views import *

urlpatterns = [
    url(r'^$', book_store),
    url(r'manage$', book_store_management),
    url(r'add_book$', add_book),
    url(r'remove_book/(?P<id>\d+)', remove_book),
    url(r'filter_by_date$', filter_by_date),
    url(r'filter_by_name$', filter_by_name),
    url(r'buy_book/(?P<id>\d+)', buy_book),
]
