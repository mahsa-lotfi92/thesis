from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajax', include('ajax_testing.urls')),
    url(r'^accounting', include('accounting.urls')),
]
