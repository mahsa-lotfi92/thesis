from django.contrib import admin

# Register your models here.
from accounting.models import Transaction


@admin.register(Transaction)
class RequestEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'is_income']