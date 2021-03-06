from django.contrib import admin

# Register your models here.
from ajax_testing.models import RequestEntry


@admin.register(RequestEntry)
class RequestEntryAdmin(admin.ModelAdmin):
    list_display = ['function_name', 'success', 'test_res']