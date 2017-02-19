from django.conf.urls import url
from django.shortcuts import render

from ajax_testing.dynamic_import import run_method
from ajax_testing.views import request_week

urlpatterns = [
    url(r'^$', lambda r: render(r, 'home.html')),
    url(r'get_week$', request_week),
    url(r'run_methods$', run_method),
]
