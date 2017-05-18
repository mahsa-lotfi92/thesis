from django.contrib import admin

# Register your models here.
from library.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'available', 'price', 'publish_date']